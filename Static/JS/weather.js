const apiKey = "450662f31eb1f71fa690707c8f527aa9";
const apiUrl = "https://api.openweathermap.org/data/2.5/weather?units=metric&q=";

const searchBox = document.querySelector(".search input");
const searchBtn = document.querySelector(".search button");
const weatherIcon = document.getElementsByClassName("weather_icon");

async function checkWeather(city){
    const response = await fetch(apiUrl + city + `&appid=${apiKey}`);
    if(response.status == 404){
        document.querySelector(".error").style.display = "block";
        document.querySelector(".weather").style.display = "none";
    }
    else{
        var data = await response.json();
        console.log(data);
        document.querySelector(".city").innerHTML = data.name;
        document.querySelector(".temp").innerHTML =Math.round(data.main.temp) + "°C";
        document.querySelector(".humidity").innerHTML = data.main.humidity + "%";
        document.querySelector(".wind").innerHTML = data.wind.speed + "km/h";
    
        if(data.weather[0].main == "Clouds"){
            weatherIcon.src = "{% static 'Images/Cloudy.jpeg' %}";
        }
        else if(data.weather[0].main == "Clear"){
            weatherIcon.src = "{% static 'Images/Sunny.jpeg' %}";
        }
        else if(data.weather[0].main == "Rain"){
            weatherIcon.src = "{% static 'Images/Rainy.jpeg' %}";
        }
        else if(data.weather[0].main == "Drizzle"){
            weatherIcon.src = "{% static 'Images/drizzle.jpeg' %}";
        }
        else if(data.weather[0].main == "Mist"){
            weatherIcon.src = "{% static 'Images/mist.jpeg' %}";
        }
        else if(data.weather[0].main == "Snow"){
            weatherIcon.src = "{% static 'Images/Snow.png' %}";
        }
    
        document.querySelector(".weather").style.display = "block";
        document.querySelector(".error").style.display = "none";
    }
}
searchBtn.addEventListener("click",()=>{
    checkWeather(searchBox.value);
})