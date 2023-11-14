var is_stop = true;
var second = 0;
var minute = 0;
var hour = 0;

function timer() {
    if (is_stop == false) {
        second = parseInt(second);
        minute = parseInt(minute);
        hour = parseInt(hour);

        second++;
        if (second == 60) {
            second = 0;
            minute++;
        }
        if (minute == 60) {
            minute = 0;
            hour++;
        }
        if (second < 10) {
            second = "0" + second;
        }
        if (minute < 10) {
            minute = "0" + minute;
        }
        if (hour < 10) {
            hour = "0" + hour;
        }

        timer_1.innerHTML = hour + " : " + minute + " : " + second;
        setTimeout("timer()", 1000);


    }
}


function start() {
    if (is_stop == true) {
        is_stop = false;
        timer();
    }
}


function stop() {
    is_stop = true;
}
function reset() {
    is_stop = true;
    second = 0;
    minute = 0;
    hour = 0;

    timer_1.innerHTML = "00 : 00 : 00";

}