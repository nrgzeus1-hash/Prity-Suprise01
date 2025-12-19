from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # यह कोड 'templates' फोल्डर के अंदर रखे index.html को खोजेगा
    return render_template('index.html')

if __name__ == '__main__':
    print("सर्वर चालू हो गया है! अब ब्राउज़र में http://127.0.0.1:5000 खोलें")
    app.run(debug=True)
