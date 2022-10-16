async function getPlant() {
    var id = 1;
    let plants = axios({
        method: 'get',
        url: 'https://agropiproject.herokuapp.com/plants/' + id
    })
        .then(function (response) {
            return response.data;
        })
        .catch(err => console.log())
        console.log( await plants)
    return await plants
}

function addPlant() {
    var name = DOMPurify.sanitize(document.getElementById('name').value);
    var species = DOMPurify.sanitize(document.getElementById('species').value);
    var lightIntensity = DOMPurify.sanitize(document.getElementById('optimalLight').value);
    var lightMargin = DOMPurify.sanitize(document.getElementById('lightMargin').value);
    var airHumidity = DOMPurify.sanitize(document.getElementById('optimalAirHumidity').value);
    var humidityMargin = DOMPurify.sanitize(document.getElementById('airHumidityMargin').value);
    var soilMoisture = DOMPurify.sanitize(document.getElementById('optimalSoilMoisture').value);
    var soilMoistureMargin = DOMPurify.sanitize(document.getElementById('soilMoistureMargin').value);
    var temperature = DOMPurify.sanitize(document.getElementById('optimalTemperature').value);
    var temperatureMargin = DOMPurify.sanitize(document.getElementById('temperatureMargin').value);

    axios.post('https://agropiproject.herokuapp.com/plants/', {name, species, lightIntensity, lightMargin, airHumidity, humidityMargin, soilMoisture, soilMoistureMargin, temperature, temperatureMargin})
        .then(res => {
            console.log(res);
        })
        .catch(err => console.log(err));
}

function updatePlant() {
    var plantName = DOMPurify.sanitize(document.getElementById(''));
    var plantKind = DOMPurify.sanitize(document.getElementById(''));

    axios({method: 'put',
    url:'',
    data: {
        plantName: plantName,
        plantKind: plantKind
    }
    })
        .then()
        .catch(err => console.log(err));
}

// DELETE REQUEST
function deletePlant(plantId) {
    axios.delete('', {
        data: {
            id: plantId
        }
    })
}

function removePlants() {
    IDs = getRows('plantTable');

    for (let i=0; i<IDs.length; i++) {
        deletePlant(IDs[i]);
    }
}


// returns a list of checked table rows
function getRows(id) {
    var tablerows = document.getElementById(id).rows;
    // console.log(tablerows[1].cells[0].children[0].checked);
    
    var res = [];   

    for (let i=1; i<tablerows.length; i++) {
        var checkbox = tablerows[i].cells[0].children[0].checked;
        var id = tablerows[i].cells[1].innerHTML;

        if (checkbox == true) {
            res.push(id);
        }
    }

    return res;
}


// Event listeners
document.getElementById('addPlant').addEventListener('click', addPlant);
document.getElementById('deletePlant').addEventListener('click', removePlants);