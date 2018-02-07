echo -n "Enter wifi SSID:   "
read ssid

echo -n "Enter wifi password:   "
read key

uci set wireless.sta.ssid=$ssid
uci set wireless.sta.key=$key
uci set wireless.sta.encryption=psk2
uci set wireless.sta.disabled=0
uci commit
wifi
