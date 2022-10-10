/*
Template Name: Skote - Admin & Dashboard Template
Author: Themesbrand
Website: https://themesbrand.com/
Contact: themesbrand@gmail.com
File: Session Timeout Js File
*/

$.sessionTimeout({
	keepAliveUrl: "../utility/starterpage",
	logoutButton: "Logout",
	logoutUrl: "../account/logout/?next=/auth-logout",
	redirUrl: "../auth-lockscreen/",
	warnAfter: 3000,
	redirAfter: 30000,
	countdownMessage: "Redirecting in {timer} seconds.",
});
$('#session-timeout-dialog  [data-dismiss=modal]').attr("data-bs-dismiss", "modal");