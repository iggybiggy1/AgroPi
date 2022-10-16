function user_plant_data(){

    const name = document.getElementById("name").value;
    const species = document.getElementById("species").value;
    const OptLight = document.getElementById("OptLight").value;
    const LightMarg = document.getElementById("LightMargin").value; 
    const OptAir = document.getElementById("OptAir")
    const AirMarg = document.getElementById("AirMargin").value;
    const OptSoil = document.getElementById("OptSoil").value;
    const SoilMarg = document.getElementById("SoilMargin").value;
    const OptTemp = document.getElementById("optimalTemperature").value; 
    const TempMarg = document.getElementById("TempMargin")
    
    const toSend = {
        name: "ASS",
        species: species,
        Optimal_light_intensity: OptLight,
        Light_intensity_margin: LightMarg,
        Optimal_air_humidity:  OptAir,
        Air_humudity_margin: AirMarg,
        Optimal_soil_moisture: OptSoil,
        Soil_moisture_margine:  SoilMarg,
        Optimal_temperature: OptTemp,
        Temperature_margin: TempMarg
    }

    const jsonString = JSON.stringify(toSend)
    console.log(jsonString)
    
    
   
    
}