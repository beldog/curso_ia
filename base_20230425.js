/*
Ejercicio: busca un nº random entre 0 y 100, muestra con
un while todos los números desde 0 al nº en cuestión.  plus plus sería css con js
let randomNum = Math.floor(Math.random() * 101);
*/
INTERVAL = 100;
i = 0;
MAX = 15;

function createListElement(interval){
    console.log("Iteración: "+ i);
    let lista = document.getElementById("numeros");
    let element = document.createElement("LI");

    let value = Math.floor(Math.random()*100);
    let children = document.getElementById("numeros").childElementCount;
    element.setAttribute("id", "element_"+children);
    element.textContent = value;
    lista.appendChild(element);
    i++;

    if(i>=MAX){
        finishProcess(interval);
    }
}

function finishProcess(interval){
    window.clearInterval(interval);

    let winner = Math.floor(Math.random()*MAX);
    let winnerElem = document.getElementById("element_"+ winner)
    winnerElem.setAttribute("class", "winner");
    console.log("Winner element is: "+ winner);
    console.log("Winner value is: "+ winnerElem.textContent);
}

window.onload = function(){
    let interval = null;
    interval = window.setInterval(function(){createListElement(interval)}, INTERVAL);
};