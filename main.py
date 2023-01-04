from website import create_app

app = create_app()

if __name__ == '__main__':
    # Ville normalt ikke kører med debug i produktionsmiljø -> Man kan også vælge port via:   app.run(debug=True, port=<desired port>)
    app.run(debug=True)
