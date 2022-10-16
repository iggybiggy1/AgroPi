function buildGraph() {
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
      size: 18
    }
  };

  Plotly.newPlot('graph1', data, layout, config);
}