from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Data portofolio bisa dimasukkan di sini
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Portfolio Saya</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <header>
        <h1>Nama Anda</h1>
        <p>Python Developer | Web Enthusiast</p>
    </header>
    <section id="about">
        <h2>Tentang Saya</h2>
        <p>Saya adalah pengembang yang fokus pada Python dan teknologi web.</p>
    </section>
    <section id="projects">
        <h2>Proyek</h2>
        <div class="project-card">Proyek 1 - Web Scraper (Python)</div>
        <div class="project-card">Proyek 2 - Flask API</div>
    </section>
</body>
</html>

body {font-family: Arial,sans-serif; margin: 0; padding: 0; background-color: #f4f4f4; text-align: center; }
header {background: #333; color: white; padding: 2rem; }
section { padding: 2rem; }
.project-card { background: white; margin: 10px; padding: 20px; border-radius: 5px; display: inline-block; width: 30%; }
