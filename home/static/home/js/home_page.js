function getMonth (n) {
    "use strict";
    switch (n) {
        case 0:
            return "January";
        case 1:
            return "February";
        case 2:
            return "March";
        case 3:
            return "April";
        case 4:
            return "May";
        case 5:
            return "June";
        case 6:
            return "July";
        case 7:
            return "August";
        case 8:
            return "September";
        case 9:
            return "October";
        case 10:
            return "November";
        case 11:
            return "December";
    }
}

function NumberDays(month, year) {
    "use strict";
    switch (month) {
        case 0:
        case 2:
        case 4:
        case 6:
        case 7:
        case 9:
        case 10:
            return 31;
        case 1:
            if (year % 4 === 0) {
                return 29;
            } else{
                return 28;
            }
            break;
        default:
            return 30;
    }
}

function showDates() {
    "use strict";
    var text = "";
    var n;
    var max = NumberDays(date.getMonth(), date.getFullYear());

    for (var i=1; i<date.getDay(); i++) {
        text += "<li></li>";
    }

    for (var j=1; j<=max; j++){
        if (j<10) {
            n = "0" + j.toString();
        } else {
            n = j.toString();
        }

        if (j===date.getDate() && date.getMonth() === DATE.getMonth()){
            text += "<li><span id=\"date\" class=\"active\">" + n + "</span></li>";
        }else {
            text += "<li>" + n + "</li>";
        }
    }
    document.getElementById("dates").innerHTML = text;
}

function getDate() {
    "use strict";
    document.getElementById("year").innerHTML = date.getFullYear();
    document.getElementById("month").innerHTML = getMonth(date.getMonth());
}

function next() {
    "use strict";
    date.setMonth(date.getMonth()+1);
    showDates();
    getDate();
}

function prev() {
    "use strict";
    date.setMonth(date.getMonth()-1);
    showDates();
    getDate();
}

var date = new Date();
var DATE = new Date();
showDates();
getDate();
