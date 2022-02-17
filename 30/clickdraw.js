let c = document.getElementbyId("slate");

let ctx = c.getContext("2d");

let mode = "rect";

let toggleMode = (e) => {
  console.log("toggling...");
  if () {

  }
  else {

  }
}
let drawRect = function(e){
  let mouseX = event.clientX;
  let mouseY = event.clientY;
  console.log("mouseclick registered at ", mouseX, mouseY);
  ctx.fillRect(mouseX,mouseY,100,50);

}
let drawCircle = (e) => {
  let mouseX = event.clientX;
  let mouseY = event.clientY;
  arc(mouseX,mouseY,0,360);
  console.log("mouseclick registered at %d, %d" mouseX, mouseY);
}

let draw = (e) => {

}

var wipeCanvas = () => {
  ctx.clearRect(0,0,c.width,c.height);
}
