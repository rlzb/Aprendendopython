import qrcode

#Dados do Wifi
ssid= "NomeDaRede"
senha = "SenhaSecreta"
tipo_seguranca = "WPA"

#formato  para QR CODE WI-FI:
#WIFI:T:<tipo_seguranca>;S:{ssid};P:{senha};;


wifi_qr = f"WIFI:T:{tipo_seguranca};S:{ssid};P:{senha};;"

#Gerar QR CODE
qr = qrcode.make(wifi_qr)

#Salvar Imagem
qr.save("wifiqrcode.png")

print("QR CODE CRIADO COM SUCESSO COMO Wi-Fi_qr_code.png")