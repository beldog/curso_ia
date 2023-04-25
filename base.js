function getDate(){
    let f = [];
    let now = new Date();

    f.push(now);
    f.push(now.getDate() +"/"+ (now.getMonth()+1) +"/"+ now.getFullYear());
    f.push(now.getFullYear() +"-"+ (now.getMonth()+1) +"-"+ now.getDate());

    return f;
}

function createListElements(total){
    let i = 0;
    let ul = document.createElement("UL");
    do{
        let li = document.createElement("LI");
        li.textContent = "A"+i;
        ul.appendChild(li);
        i++;
    }while(i<total);
    document.body.appendChild(ul);
}

window.onload = function(){
    // Mostramos la fecha actual
    let tagElement = document.getElementById("fecha");
    let timeElement = document.createElement("time")
    let fecha = getDate();

    timeElement.innerText = fecha[1];
    timeElement.setAttribute("datetime", fecha[2]);
    tagElement.appendChild(timeElement);

    // Mostramos el saludo en base a la hora
    let saludoElement = document.getElementById("saludo");
    let f = fecha[0];
    if(f.getHours()>=6 && f.getHours()<13){
        saludoElement.innerText = "Buenos días";
    }
    else if(f.getHours()>=13 && f.getHours()<21){
        saludoElement.innerText = "Buenas tardes";
    }
    else{
        saludoElement.innerText = "Buenas noches";
    }

    // Mostramos el día de la semana
    let diasemanaElement = document.getElementById("dia_semana");
    let dia = "domingo";
    switch (f.getDay()){
        case 1:
            dia = "lunes";
            break;
        case 2:
            dia = "martes";
            break;
        case 3:
            dia = "miércoles";
            break;
        case 4:
            dia = "jueves";
            break;
        case 5:
            dia = "viernes";
            break;
        case 6:
            dia = "sábado";
            break;
    }
    diasemanaElement.textContent = dia;

    // Mostramos el día de la semana en el idioma español de ESPAÑA
    // ref: https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Date/toLocaleDateString
    let options = { weekday: 'long'};
    console.log(f.toLocaleDateString("es-ES", options));

    //Creamos una lista dinámica con un DO-WHILE de 10 elementos
    createListElements(10);
}