from app import setup

if __name__ == '__main__':
    app = setup()
    app.run(debug=True, host='0.0.0.0', port=5000)
