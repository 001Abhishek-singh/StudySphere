// (04/11/23) In this session we are going to create a currency converter by using the html,css & javascript.
const conversion_div_1 = document.getElementById("currency-first");
const conversion_div_2 = document.getElementById("currency-second");
const worth_first = document.getElementById("worth-first");
const worth_second = document.getElementById("worth-second");
const exchange_rate = document.getElementById("exchange-rate");

converterCurrency()

function converterCurrency(){
    fetch(`https://v6.exchangerate-api.com/v6/48de4226c7d8b2820909ea5a/latest/${conversion_div_1.value}`)
        .then((response) => response.json())
        .then((data) => {const rate = data.conversion_rates[conversion_div_2.value];
            console.log(rate);
        exchange_rate.innerText = `1 ${conversion_div_1.value} =  ${rate + " " + conversion_div_2.value}`;
            
        worth_second.value = (worth_first.value * rate).toFixed(3);
    });
}
conversion_div_1.addEventListener("change",converterCurrency)
conversion_div_2.addEventListener("change",converterCurrency)
worth_first.addEventListener("change",converterCurrency)
