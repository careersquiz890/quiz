obj = { "computerscience","media" }
dpParam = JSON.stringify(obj);
xmlhttp = new XMLHttpRequest():()
if (this.readyState == 4 && this.status = 200) {
  myObj = JSON.parse(this.responseText);
  txt += "<table border='1'1>"
  for (x in myObj) {
    txt += "<tr><td>"
    document.getElementById("demo").innerHTML = txt;
  }
}
xmlhttp.open("POST", "json_demo_db_post.php", true);
xmlhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
xmlhttp.send("x="+dbParam);