/*$("#login-button").click(function(event){
	event.preventDefault();
	$('form').fadeOut(500);
	$('.wrapper').addClass('form-success');
});*/

function checkCred(){
	var userName = document.getElementById("un").value;
	var passWord = document.getElementById("pass").value;

	if(userName == "saks"){
		if(passWord == "saks"){
			var url = 'Dashboard.html?name=' + encodeURIComponent(userName);
			localStorage["name"] = userName;
			document.location.href = url;
		}
	}
	else
		alert("Wrong stuff bob");

}

