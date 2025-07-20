import qrcode

#Dados do Wifi
ssid= "NomeDaRede"
senha = "SenhaSecreta"
tipo_seguranca = "WPA"

#formato  para QR CODE WI-FI:
#WI-FI:T:<tipo_seguranca>;S:{ssid};P:{senha};;


wifi_qr = f"WIFI:T:{tipo_seguranca};S:{ssid}:P{senha};;"

#Gerar QR CODE
qr = qrcode.make(wifi_qr)

#Salvar Imagem
qr.save("Wi-Fi_qr_code.pgn")

print("QR CODE CRIADO E SALVO COMO Wi-Fi_qr_code.png")