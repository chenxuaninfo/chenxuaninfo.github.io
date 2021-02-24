function getNowFormatDate() { //获取当前时间
	var date = new Date();
	var seperator1 = "-";
	var seperator2 = ":";
	var month = date.getMonth() + 1 < 10 ? "0" + (date.getMonth() + 1) : date.getMonth() + 1;
	var strDate = date.getDate() < 10 ? "0" + date.getDate() : date.getDate();
	var currentdate = date.getFullYear() + seperator1 + month + seperator1 + strDate +
		" " + date.getHours() + seperator2 + date.getMinutes() +
		seperator2 + date.getSeconds();
	var a = new Array("日", "一", "二", "三", "四", "五", "六");
	var week = new Date().getDay();
	document.getElementById("time").innerHTML =  "星期"+a[week]+"  "+currentdate;
	return currentdate;

}
$(document).ready(function() {
	window.setInterval("getNowFormatDate()", 1000);
});