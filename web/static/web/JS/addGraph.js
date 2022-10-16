var graphCount = 1;
var graphsTop = 1;

function addGraph() {
  if (graphCount < 4) {
    const div = document.createElement('div');
    const div2 = document.createElement('div');
    const div3 = document.createElement('div');

    const buttons = `<button onclick="removeGraph(this.parentElement.id)">delete</button>
    <select onchange="loadGraph(this.value, this.parentElement.lastChild.id)">
                        <option value="air_temperature">Air temperature</option>
                        <option value="air_humidity">Air humidity</option>
                        <option value="soil_moisture">Soil moisture</option>
                        <option selected value="light_intensity">Light intensity</option>
                    </select>`;

    let id = "graph" + (1 + graphCount);

    if (graphsTop < 2) {
      div.className = 'col-lg';
      div.id = 'graph-container' + (1 + graphCount);

      div.innerHTML = buttons;

      div.appendChild(div2);
    } else if (graphCount == 2) {
      div.className = 'row';
      div.id = 'row2';
      div.style = "height: 50%";
      div3.className = 'col-lg';
      div3.id = 'graph-container' + (1 + graphCount);
      div3.innerHTML = buttons;
      div.appendChild(div3);
      div3.appendChild(div2);
    } else {
      div3.className = 'col-lg';
      div3.id = 'graph-container' + (1 + graphCount);
      div3.innerHTML = buttons;
      div3.appendChild(div2);
    }

    div2.id = id;

    if (graphsTop < 2) {
      document.getElementById('row1').appendChild(div);
      graphsTop++;
    } else if (graphCount == 2) {
      document.getElementById('graph-container').appendChild(div);
    } else {
      document.getElementById('row2').appendChild(div3);
    }

    buildGraph(id);
    if (graphsTop == 2) {
      buildGraph('graph1');
    }

    if (graphCount == 3) {
      buildGraph('graph3');
    }

    graphCount++;
    console.log("created graph with id: " + id);
    console.log("graphcount: " + graphCount);
  }
}

function removeGraph(graph) {
  console.log("try to delete graph with id: " + graph);
  if (graphCount > 0) {
    if (graphCount == 3 && graph == 'graph-container3' && document.getElementById('graph-container4') == null) {
      var elem = document.getElementById(graph);
      elem.parentNode.remove();
    } else {
      var elem = document.getElementById(graph);
      elem.parentNode.removeChild(elem);
    }

    buildGraph('graph1');
    if (document.getElementById('graph3') != null) {
      buildGraph('graph3');
    }
    if (document.getElementById('graph4') != null) {
      buildGraph('graph4');
      document.getElementById('graph4').id = 'graph3';
      document.getElementById('graph3').parentElement.id = 'graph-container3';
    }

    if (document.getElementById('graph2') != null) {
      graphsTop = 2;
    } else {
      graphsTop = 1;
    }

    // if (graphCount == 4) {
    //   buildGraph('graph3');
    // }
    graphCount--;
    console.log("graphcount: " + graphCount);
  }
}