echo -n "Enter wifi SSID:   "
read ssid

echo -n "Enter wifi password:   "
read key

uci set wireless.sta.ssid=$ssid
uci set wireless.sta.key=$key
uci set wireless.sta.encryption=psk2
uci commit
wifi_mode sta
