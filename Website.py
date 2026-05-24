from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Generic Website</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 0; padding: 0; background: #f4f4f4; }
        header { background: white; padding: 20px; display: flex; justify-content: space-between; align-items: center; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
        nav a { margin: 0 10px; text-decoration: none; color: #333; }
        .hero { padding: 60px; text-align: center; background: #dbeafe; }
        .section { padding: 40px; background: white; margin: 10px; }
        .services { display: flex; gap: 10px; }
        .card { flex: 1; padding: 20px; background: #fff; border: 1px solid #ddd; border-radius: 10px; }
        footer { text-align: center; padding: 20px; background: #111827; color: white; }
        input, textarea { width: 100%; padding: 10px; margin: 5px 0; }
        button { padding: 10px 20px; background: green; color: white; border: none; cursor: pointer; }
    </style>
</head>
<body>

<header>
    <h2>My Python Website</h2>
    <nav>
        <a href="#home">Home</a>
        <a href="#about">About</a>
        <a href="#services">Services</a>
        <a href="#contact">Contact</a>
    </nav>
</header>

<section id="home" class="hero">
    <h1>Welcome to My Website</h1>
    <p>A simple website built with Python Flask</p>
</section>

<section id="about" class="section">
    <h2>About</h2>
    <p>This is a basic website created using Python and Flask.</p>
</section>

<section id="services" class="section">
    <h2>Services</h2>
    <div class="services">
        <div class="card">Service 1</div>
        <div class="card">Service 2</div>
        <div class="card">Service 3</div>
    </div>
</section>

<section id="contact" class="section">
    <h2>Contact</h2>
    <form method="POST" action="/contact">
        <input name="name" placeholder="Your Name" required>
        <input name="email" placeholder="Your Email" required>
        <textarea name="message" placeholder="Your Message" required></textarea>
        <button type="submit">Send</button>
    </form>
</section>

<footer>
    <p>© My Python Flask Website</p>
</footer>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(PAGE)

@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")

    print(f"New message from {name} ({email}): {message}")

    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
