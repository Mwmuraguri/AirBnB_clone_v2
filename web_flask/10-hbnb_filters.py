#!/usr/bin/python3
from flask import Flask, render_template
from models import storage

app = Flask(__name__)

defteardown_appcontext(error):
    storage.close()

@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    states = storage.all('State')
    cities = []
    amenities = storage.all('Amenity')

    for state in states:
        cities.extend([city for city in state.cities])

    cities.sort(key=lambda city: city.name)
    amenities.sort(key=lambda amenity: amenity.name)

    return render_template('10-hbnb_filters.html', states=states, cities=cities, amenities=amenities)

if __name__ == '__main__':
    app.teardown_appcontext(teardown_appcontext)
    app.run(host='0.0.0.0', port=5000, debug=True)
