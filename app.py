from flask import Flask, request, jsonify
from google_sheets import get_all_climbs, get_google_sheet

app = Flask(__name__)

@app.route('/getClimbs', methods=['GET'])
def get_climbs():
    climbs = get_all_climbs()
    return jsonify(climbs)

@app.route('/updateClimb', methods=['POST'])
def update_climb():
    request_data = request.json
    climb_name = request_data.get('climb_name')
    user = request_data.get('user')
    completed = request_data.get('completed')

    sheet = get_google_sheet()
    data = sheet.get_all_records()

    # Find the row to update based on climb_name
    for i, row in enumerate(data):
        if row['Name'] == climb_name:
            cell_col = None
            # Find the column for the user
            for col_index, header in enumerate(sheet.row_values(1)):
                if header == user:
                    cell_col = col_index + 1
                    break

            if cell_col:
                # Update the cell in the corresponding user column
                sheet.update_cell(i + 2, cell_col, '✔' if completed else '')

            break

    return jsonify({"message": f"Updated climb {climb_name} for {user}"})

if __name__ == '__main__':
    app.run(debug=True)
