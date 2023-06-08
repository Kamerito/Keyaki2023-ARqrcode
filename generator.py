import qrcode

def generate_qr_code(obj_file, artwork_name):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(f'obj_file:{obj_file};artwork_name:{artwork_name}')
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save("作品名-qrcode.png")

# ここにデータを追加
generate_qr_code("〇〇.obj", "作品名")
