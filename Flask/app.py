from flask import Flask, render_template, request

app = Flask(__name__)

NUM_FLOORS = 10
ROOMS_PER_FLOOR = 2
MAX_ROOMS = NUM_FLOORS * ROOMS_PER_FLOOR
room_occupancy = [False] * MAX_ROOMS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/reserve', methods=['POST'])
def reserve():
    floor_choice = int(request.form['floor'])
    room_number = assign_room(floor_choice)
    if room_number == -1:
        return render_template('no_rooms_available.html')
    else:
        guest_name = request.form['guest_name']
        duration_of_stay = int(request.form['duration_of_stay'])
        allergies = request.form['allergies']

        room_occupancy[room_number - 1] = True

        return render_template('reservation.html', guest_name=guest_name, room_number=room_number, floor=floor_choice, duration_of_stay=duration_of_stay, allergies=allergies)

def assign_room(floor):
    start_room = (floor - 1) * ROOMS_PER_FLOOR + 1
    for i in range(start_room, start_room + ROOMS_PER_FLOOR):
        if not room_occupancy[i - 1]:
            return i
    return -1

if __name__ == '__main__':
    app.run(debug=True)
