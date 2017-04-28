var suggest = function(str) {
    if( str.length == 0){
	document.getElementById("handle").innerHTML =" ";
	return;
    }
    url = "http://127.0.0.1:8000/han"
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
	if (this.readyState == 4 && this.status == 200) {
	    document.getElementById("hint").innerHTML = this.responseText;
	}
    };
    p = {handle:str};
    var t = JSON.stringify(p);
    console.log(t);
    xhttp.open("POST",url,true);
    xhttp.setRequestHeader("Content-type","application/json");
    xhttp.send(t);      
}
document.getElementById("button").disabled = true;
enable();
var match = function(str) {
    console.log(document.getElementById('usr_pass').value);
    console.log(document.getElementById('usr_pass_conf').value);
    if( document.getElementById("usr_pass").value === str )
    {
	document.getElementById("no").innerHTML = "";
	enable();
    }
    else
    {
	document.getElementById("no").innerHTML = "passwords don't match";
	document.getElementById("button").disabled = true;
	enable();
    }
    console.log(document.getElementById("usr_pass").value === str);
}

var length = function(str) {
    if(str.length < 8)
	document.getElementById("len").innerHTML = "password must be atleast 8 characters long";
    else
	document.getElementById("len").innerHTML = "";
    enable();
}
var match2 = function(str) {
    if( document.getElementById("usr_pass_conf").value === str )
    {
	document.getElementById("no").innerHTML = "";
	enable();
    }
    else
    {
	document.getElementById("no").innerHTML = "passwords don't match";
	enable();
    }
    console.log(document.getElementById("usr_pass").value === str);
    length(str);
}


var enable = function(){
    if(document.getElementById("no").value == "" && document.getElementById("len").value == "" && document.getElementById("hint") == 'ok')
	document.getElementById("button").disabled = false;
}
