var bars = document.querySelectorAll(".bar");
var total = Number(bars[0].getAttribute('value'));

var width = 0;

for(var i of bars){
    width = Math.round(Number(i.getAttribute('value')/total)*100)+'%';
    i.style.width = width;
}

bars[0].style.background = "#decade";
bars[1].style.background = "#5CEEE6";
bars[2].style.background = "#FFD5D2";
bars[3].style.background = "#DEEASD";