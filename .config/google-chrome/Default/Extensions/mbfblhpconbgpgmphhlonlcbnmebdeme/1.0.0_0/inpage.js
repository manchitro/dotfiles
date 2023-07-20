"use strict";
/*global chrome: true*/

let targetElement = null;

document.addEventListener("mousedown", e =>
{
	if(e.button===2)
		targetElement = e.target;
}, true);

chrome.runtime.onMessage.addListener(function messageListener(r)
{
	if(!targetElement || !r)
		return;

	const alterAngleBy = (r.dir==="left" ? -90 : 90);
	if(targetElement.style && targetElement.style.transform && targetElement.style.transform.length>0)
		targetElement.style.transform = targetElement.style.transform.split(")").map(v => ((v.indexOf("rotate(")===0) ? ("rotate(" + ((+v.match(/rotate\(([0-9]+)deg\)?/)[1]) + alterAngleBy) + "deg") : v)).join(") ").trim();
	else
		targetElement.style.transform = "rotate(" + alterAngleBy + "deg)";
});
