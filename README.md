# Auto_Notifications

Aviso automatico de stock para la mochila **Kailas Fuga AIR 8** (tallas M y L).
Consulta el endpoint `.js` de Shopify (disponibilidad real por variante) y manda
un push a [ntfy.sh](https://ntfy.sh) cuando alguna talla objetivo vuelve a estar disponible.

## Puesta en marcha
1. Instala la app **ntfy** en el movil y suscribete a un topic unico.
2. Edita `NTFY_TOPIC` en `check_stock.py` con ese topic.
3. (Opcional) Ajusta `TARGETS` para cambiar las tallas vigiladas.
4. Push a este repo: GitHub Actions lo ejecuta segun el cron de
   `.github/workflows/stock-check.yml` (cada 15 min por defecto).

## Ejecutar en local
```bash
python check_stock.py
```

## Notas
- GitHub Actions no garantiza intervalos < 5 min y puede retrasarse en horas punta.
- Para fiabilidad al minuto, usa un cron local o un VPS con el mismo script.
