const margin = {top:0, right: 0, bottom: 0, left: 0},
width = 300 - margin.left - margin.right;
height = 500 - margin.top - margin.bottom;

// d3.json("https://thawing-anchorage-76337.herokuapp.com/plants/1", function(data) {
//         console.log(data[0].id);
//     });

// var maxValue = d3.max();
// var minValue;
// var maxTime;
// var minTime;

const svg = d3.select("#graph1")
    .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
    .append("g")
        .attr("transform", `translate(${margin.left},${margin.top})`);

// const parseDate = d3.time.format().parse;

var	x = d3.time.scale().range([0, width]);
var	y = d3.scale.linear().range([height, 0]);