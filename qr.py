import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

my_qrcode=qrcode.make("https://www.youtube.com/watch?v=DbiRVNeZPnw&list=RDDbiRVNeZPnw&start_radio=1")
qr1=qrcode.make("https://www.hotstar.com/in/onboarding/profile?utm_source=jiocinema&ref=%2Fin%2Fhome%3Futm_source%3Djiocinema")
qr1.save("Web qr.png")

my_qrcode.save("my_qrcode.png",scale= 8)

bs=decode(Image.open("my_qrcode.png"))
print(bs[0].data.decode("ascii"))