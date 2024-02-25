function generate_evidance(){
    var xhttp = new XMLHttpRequest();
    //prompt = document.getElementById('eprompt')
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
          document.getElementById("demo").innerHTML = this.responseText;
        }
      };
      //data = {"data": {'prompt': prompt}}
      xhttp.open("GET", "/gen_evidance", true);
      xhttp.send();
}