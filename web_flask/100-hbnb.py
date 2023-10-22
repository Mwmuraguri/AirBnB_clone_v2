#!/usr/bin/python3
from flask import Flask, render_template
from models import storage

app = Flask(__name__)

defteardown_appcontext(error):
    storage.close()

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    states = storage.all('State')
    cities = []
    amenities = storage.all('Amenity')
    places = storage.all('Place')

    for state in states:
        cities.extend([city for city in state.cities])

    cities.sort(key=lambda city: city.name)
    amenities.sort(key=lambda amenity: amenity.name)
    places.sort(key=lambda place: place.name)

    return render_template('100-hbnb.html', states=states, cities=cities, amenities=amenities, places=places)

if __name__ == '__main__':
    app.teardown_appcontext(teardown_appcontext)
    app.run(host='0.0.0.0', port=5000, debug=True)
