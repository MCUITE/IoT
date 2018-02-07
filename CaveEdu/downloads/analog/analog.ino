void setup()
{
    Serial.begin(9600);
    Serial1.begin(9600);
    pinMode(A0, INPUT);
}

void loop()
{
    int value = analogRead(A0);
    Serial.println(value);
    Serial1.println(value);
    delay(1000);
}
