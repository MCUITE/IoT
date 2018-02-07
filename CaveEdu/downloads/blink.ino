int led = 13;

void setup() {         
    // initialize the digital pin as an output
    // Pin 13 has an LED connected on board
	pinMode(13, OUTPUT); 
}

void loop() {	
    digitalWrite(led, HIGH);   // set the LED on
    delay(1000);               // wait for a second
    digitalWrite(led, LOW);    // set the LED off
    delay(1000);               // wait for a second
}


