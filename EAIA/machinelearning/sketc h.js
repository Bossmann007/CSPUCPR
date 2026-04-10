let video;
let label = "Aguardando...";
let classifier;

let modelURL = 'https://teachablemachine.withgoogle.com/models/uMch9ZVgt/';

function preload() {
  classifier = ml5.imageClassifier(modelURL + 'model.json');
}

function setup() {
  createCanvas(640, 520);
  video = createCapture(VIDEO);
  video.hide();
  classifyVideo();
}

function classifyVideo() {
  classifier.classify(video, gotResults);
}

function draw() {
  background(0);
  image(video, 0, 0);

  let emoji   = "❓";
  let bgColor = color(30, 30, 30);

  if (label == "Feliz") {
    emoji   = "😄";
    bgColor = color(255, 200, 0);
  } else if (label == "Bravo") {
    emoji   = "😠";
    bgColor = color(220, 50, 50);
  } else if (label == "Surpreso") {
    emoji   = "😲";
    bgColor = color(100, 100, 220);
  }

  noStroke();
  fill(bgColor);
  rect(0, 455, 640, 65);

  fill(255);
  textSize(28);
  textAlign(CENTER, CENTER);
  text(label, width / 2, 483);

  textSize(200);
  text(emoji, width / 2, height / 2.2);
}

function gotResults(error, results) {
  if (error) {
    console.error(error);
    return;
  }
  label = results[0].label;
  classifyVideo();
}