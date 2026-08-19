#!/usr/bin/env python3
"""
Avisa cuando la Kailas Fuga AIR 8 vuelve a tener stock en M o L.
Consulta el endpoint .js de Shopify (disponibilidad real por variante)
y envia un push a ntfy.sh si alguna talla objetivo esta disponible.
"""
import sys
import urllib.request

PRODUCT_JS = (
    "https://www.kailasfuga.com/products/"
    "the-fuga-big-test-kailas-fuga-air-8-air-7-trail-running-vest-pack.js"
)
PRODUCT_URL = (
    "https://www.kailasfuga.com/products/"
    "the-fuga-big-test-kailas-fuga-air-8-air-7-trail-running-vest-pack"
)

# Tallas que te interesan (segun el campo "title" de cada variante).
TARGETS = {"AIR 8 / M", "AIR 8 / L"}

# Canal de ntfy: elige un nombre unico y suscribete en la app ntfy.
NTFY_TOPIC = "kailas-air8-adria"

HEADERS = {"User-Agent": "Mozilla/5.0 (stock-checker)"}


def fetch_variants():
    req = urllib.request.Request(PRODUCT_JS, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=20) as r:
        import json
        return json.load(r).get("variants", [])


def notify(available):
    tallas = ", ".join(v["title"] for v in available)
    body = f"Disponible: {tallas}\n{PRODUCT_URL}"
    req = urllib.request.Request(
        f"https://ntfy.sh/{NTFY_TOPIC}",
        data=body.encode("utf-8"),
        headers={
            "Title": "Kailas AIR 8 en stock",
            "Priority": "high",
            "Tags": "running_shirt,tada",
            "Click": PRODUCT_URL,
        },
    )
    urllib.request.urlopen(req, timeout=20)


def main():
    variants = fetch_variants()
    available = [
        v for v in variants
        if v.get("title") in TARGETS and v.get("available")
    ]
    for v in variants:
        if v.get("title") in TARGETS:
            estado = "DISPONIBLE" if v.get("available") else "agotada"
            print(f"{v['title']}: {estado}")
    if available:
        notify(available)
        print(">> Aviso enviado.")
        sys.exit(0)
    print(">> Nada aun.")


if __name__ == "__main__":
    main()
