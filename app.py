import os # Tambahkan ini di paling atas
import requests
from flask import Flask, render_template

app = Flask(__name__)

# Nomor WhatsApp yang Anda berikan
NOMOR_WA = "6281318900348"

def get_products():
    # Menambahkan ?limit=250 untuk mengambil lebih banyak produk (maksimal Shopify)
    url = "https://910.id/collections/all/products.json?limit=250"
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json().get('products', [])
        return []
    except Exception as e:
        print(f"Error: {e}")
        return []

@app.route('/')
def index():
    products = get_products()
    return render_template('index.html', products=products, wa_number=NOMOR_WA)

# ... kode lainnya tetap sama ...

if __name__ == '__main__':
    # Render membutuhkan port dinamis
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)