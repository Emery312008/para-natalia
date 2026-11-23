import webbrowser
import os

html = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Para Natalia</title>
    <style>
        body {
            margin: 0;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            background: linear-gradient(#fff5f8, #ffe0ea);
            font-family: "Georgia", serif;
        }
        canvas {
            max-width: 90vw;
        }
        h1 {
            color: #c2185b;
            font-size: 2.2em;
            margin-top: 10px;
            animation: aparecer 2s ease-in;
        }
        @keyframes aparecer {
            from { opacity: 0; transform: translateY(20px); }
            to   { opacity: 1; transform: translateY(0); }
        }
    </style>
</head>
<body>
    <canvas id="flor" width="600" height="600"></canvas>
    <h1>Te amo Natalia</h1>

    <script>
        const canvas = document.getElementById("flor");
        const ctx = canvas.getContext("2d");
        const cx = 300, cy = 300;

        function petalo(angulo, largo, ancho, color) {
            ctx.save();
            ctx.translate(cx, cy);
            ctx.rotate(angulo);
            ctx.beginPath();
            ctx.moveTo(0, 0);
            ctx.bezierCurveTo(ancho, -largo * 0.3, ancho, -largo, 0, -largo);
            ctx.bezierCurveTo(-ancho, -largo, -ancho, -largo * 0.3, 0, 0);
            ctx.fillStyle = color;
            ctx.fill();
            ctx.strokeStyle = "rgba(180, 30, 90, 0.5)";
            ctx.lineWidth = 1.5;
            ctx.stroke();
            ctx.restore();
        }

        function dibujarFlor() {
            // Pétalos exteriores
            const capas = [
                { n: 8,  largo: 230, ancho: 75, color: "#f8bbd0", offset: 0 },
                { n: 8,  largo: 190, ancho: 65, color: "#f48fb1", offset: Math.PI / 8 },
                { n: 6,  largo: 150, ancho: 55, color: "#f06292", offset: 0 },
                { n: 5,  largo: 105, ancho: 42, color: "#ec407a", offset: Math.PI / 5 },
            ];

            capas.forEach(capa => {
                for (let i = 0; i < capa.n; i++) {
                    const ang = (Math.PI * 2 / capa.n) * i + capa.offset;
                    petalo(ang, capa.largo, capa.ancho, capa.color);
                }
            });

            // Centro amarillo
            ctx.beginPath();
            ctx.arc(cx, cy, 42, 0, Math.PI * 2);
            ctx.fillStyle = "#fdd835";
            ctx.fill();

            // Puntitos del centro
            ctx.fillStyle = "#f9a825";
            for (let i = 0; i < 30; i++) {
                const a = Math.random() * Math.PI * 2;
                const r = Math.random() * 32;
                ctx.beginPath();
                ctx.arc(cx + Math.cos(a) * r, cy + Math.sin(a) * r, 2.5, 0, Math.PI * 2);
                ctx.fill();
            }
        }

        // Animación: los pétalos se dibujan uno por uno
        let progreso = 0;
        const total = 1;
        function animar() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            progreso += 0.01;
            dibujarFlorParcial(Math.min(progreso, total));
            if (progreso < total) requestAnimationFrame(animar);
        }

        function dibujarFlorParcial(p) {
            // Versión sencilla: escala la flor completa desde el centro
            ctx.save();
            ctx.translate(cx, cy);
            ctx.scale(p, p);
            ctx.translate(-cx, -cy);
            dibujarFlor();
            ctx.restore();
        }

        animar();
    </script>
</body>
</html>
"""

ruta = os.path.abspath("flor_natalia.html")
with open(ruta, "w", encoding="utf-8") as f:
    f.write(html)

print("Página creada en:", ruta)
webbrowser.open("file://" + ruta)
