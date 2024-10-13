const textbox = document.getElementById("text-box");
const listbox = document.getElementById("list-container")

function addtask(){
    if(textbox.value === ''){
        alert("You cannot leave empty...");
    }
    else{
        let li = document.createElement("li");// creating a li tag and stored that tag into the li variable
        li.innerHTML = textbox.value; // storing the value from input into the li variable too
        listbox.appendChild(li); // append the li tag and its value into the listbox variable or list-container.
        let span = document.createElement("span");
        span.innerHTML = "\u00d7";
        li.appendChild(span);
    }
    textbox.value = "";
    saveData()
}

listbox.addEventListener("click",function(e){
    if(e.target.tagName === "LI"){
        e.target.classList.toggle("checked");
        saveData()
    }
    else if(e.target.tagName === "SPAN"){
        e.target.parentElement.remove();
        saveData()
    }
},false);

function saveData(){
    localStorage.setItem("data",listbox.innerHTML);
}
function showTask(){
    listbox.innerHTML = localStorage.getItem("data");
}
showTask();