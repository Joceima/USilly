from flask import Flask
from website import createApp

app = createApp()

# only if you start it from this file
if __name__ == "__main__":
    app.run(debug=True)
