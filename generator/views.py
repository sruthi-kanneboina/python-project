from django.shortcuts import render
import qrcode
import io
import base64

def generate_qr(request):
    qr_image = None
    if request.method == "POST":
        data = request.POST.get("data")
        if data:
            # Create QR code
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(data)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")

            # Convert to base64
            buffer = io.BytesIO()
            img.save(buffer, format="PNG")
            img_b64 = base64.b64encode(buffer.getvalue()).decode("utf-8")
            qr_image = f"data:image/png;base64,{img_b64}"

    return render(request, "index.html", {"qr_image": qr_image})

