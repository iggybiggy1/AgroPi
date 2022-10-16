xValues = [1,2,3,4,5,6]
yValues = []

dataPoints = "{{dataPoints}}";

for (dp in dataPoints) {
    // xValues.push();
    yValues.push(dp.air_humidity);
}

console.log("{{dataPoints}}");
var trace1 = {
    x: xValues,
    y: yValues,
    type: 'scatter'
  };
  
  var data = [trace1];
  
  Plotly.newPlot('graph1', data);
  