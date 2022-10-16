function buildGraph(graphId) {
  console.log("build: " + graphId);

  var config = {
    responsive: true
  }

  var trace1 = {
    x: xValues,
    y: yValues,
    type: 'scatter'
  };

  var data = [trace1];

  var layout = {
    title: '',
    font: {
      size: 12
    }
  };

  Plotly.newPlot(graphId, data, layout, config);
}