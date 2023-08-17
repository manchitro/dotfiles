from dbus_next.aio import MessageBus
from dbus_next.constants import BusType

from libqtile.widget import base

BLUEZ = "org.bluez"
BLUEZ_PATH = "/org/bluez/hci0"
BLUEZ_ADAPTER = "org.bluez.Adapter1"
BLUEZ_DEVICE = "org.bluez.Device1"
BLUEZ_PROPERTIES = "org.freedesktop.DBus.Properties"


class BtIndicator(base._TextBox):
    """
    Displays bluetooth status for a particular connected device.

    (For example your bluetooth headphones.)

    Uses dbus-next to communicate with the system bus.

    Widget requirements: dbus-next_.

    .. _dbus-next: https://pypi.org/project/dbus-next/
    """

    defaults = [
        (
            "hci",
            "/dev_XX_XX_XX_XX_XX_XX",
            "hci0 device path, can be found with d-feet or similar dbus explorer.",
        )
    ]

    def __init__(self, **config):
        base._TextBox.__init__(self, "", **config)
        self.add_defaults(BtIndicator.defaults)

    async def _config_async(self):
        # set initial values
        self.powered = await self._init_adapter()
        self.connected, self.device = await self._init_device()

        self.update_text()

    async def _init_adapter(self):
        # set up interface to adapter properties using high-level api
        bus = await MessageBus(bus_type=BusType.SYSTEM).connect()
        introspect = await bus.introspect(BLUEZ, BLUEZ_PATH)
        obj = bus.get_proxy_object(BLUEZ, BLUEZ_PATH, introspect)
        iface = obj.get_interface(BLUEZ_ADAPTER)
        props = obj.get_interface(BLUEZ_PROPERTIES)

        powered = await iface.get_powered()
        # subscribe receiver to property changed
        props.on_properties_changed(self._signal_received)
        return powered

    async def _init_device(self):
        # set up interface to device properties using high-level api
        bus = await MessageBus(bus_type=BusType.SYSTEM).connect()
        introspect = await bus.introspect(BLUEZ, BLUEZ_PATH + self.hci)
        obj = bus.get_proxy_object(BLUEZ, BLUEZ_PATH + self.hci, introspect)
        iface = obj.get_interface(BLUEZ_DEVICE)
        props = obj.get_interface(BLUEZ_PROPERTIES)

        connected = await iface.get_connected()
        name = await iface.get_name()
        # subscribe receiver to property changed
        props.on_properties_changed(self._signal_received)
        return connected, name

    def _signal_received(self, interface_name, changed_properties, _invalidated_properties):
        powered = changed_properties.get("Powered", None)
        if powered is not None:
            self.powered = powered.value
            self.update_text()

        connected = changed_properties.get("Connected", None)
        if connected is not None:
            self.connected = connected.value
            self.update_text()

        device = changed_properties.get("Name", None)
        if device is not None:
            self.device = device.value
            self.update_text()

    def update_text(self):
        text = ""
        if not self.powered:
            text = ""
        else:
            if not self.connected:
                text = ""
            else:
                text = "🎧"
        self.update(text)
