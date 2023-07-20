"use strict";
/*global chrome: true*/

chrome.contextMenus.removeAll(() =>
{
	chrome.contextMenus.create({ title : "Rotate", contexts : ["image"], visible : true, id : "rotate"}, () =>
	{
		["Right", "Left"].forEach(dir =>
		{
			chrome.contextMenus.create({
				title    : dir,
				contexts : ["image"],
				visible  : true,
				parentId : "rotate",
				id       : "rotate" + dir.toLowerCase(),
				onclick  : (eventInfo, tab) => chrome.tabs.sendMessage(tab.id, {dir : dir.toLowerCase()}) });
		});
	});
});
