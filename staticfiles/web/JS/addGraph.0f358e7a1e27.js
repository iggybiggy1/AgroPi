function addRow() {
    const div = document.createElement('div');
  
    div.className = 'col-lg';

    let id = "graph4";
  
    div.innerHTML = `<p>hello there</p>`;
  
    document.getElementById('row1').appendChild(div);
    buildGraph();
  }
  
  function removeRow(input) {
    document.getElementById('row1').removeChild(input.parentNode);
  }