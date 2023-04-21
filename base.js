function getDate(){
    let f = [];
    let now = new Date();

    f.push(now.getDate() +"/"+ (now.getMonth()+1) +"/"+ now.getFullYear());
    f.push(now.getFullYear() +"-"+ (now.getMonth()+1) +"-"+ now.getDate());

    return f;
}

window.onload = function(){
    // Mostramos la fecha actual
    let tagElement = document.getElementById("fecha");
    let timeElement = document.createElement("time")
    let fecha = getDate();

    timeElement.innerText = fecha[0];
    timeElement.setAttribute("datetime", fecha[1]);
    tagElement.appendChild(timeElement);

    // Mostramos el saludo en base a la hora
    let saludoElement = document.getElementById("saludo");
    let f = new Date();

    if(f.getHours()>=6 && f.getHours()<13){
        saludoElement.innerText = "Buenos días";
    }
    else if(f.getHours()>=13 && f.getHours()<21){
        saludoElement.innerText = "Buenas tardes";
    }
    else{
        saludoElement.innerText = "Buenas noches";
    }
}