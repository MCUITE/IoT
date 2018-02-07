var m = require('mraa');
var ledStatus = true;
var led = new m.Gpio(44);

led.dir(m.DIR_OUT);

function blink() {
    led.write(ledStatus ? 1:0);
    ledStatus = !ledStatus;
    setTimeout(blink, 100);
}

blink();



