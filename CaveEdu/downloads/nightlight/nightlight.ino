void setup()
{
    pinMode(13, OUTPUT);
    pinMode(A0, INPUT);
    Serial.begin(9600);
}

void loop()
{
    while(!Serial.available())
    {
        int light = analogRead(A0);
        Serial.println(light);
        digitalWrite(13, (light < 1023) ? HIGH : LOW);
    }
}



