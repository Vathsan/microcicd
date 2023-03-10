from flask import Flask

doctors = [{
    "id": 1,
    "name": "Jeremy Willey",
    "hospital": "Green Country Community Hospital",
    "speciality": "Surgery"
},
    {
    "id": 2,
    "name": "Camille Modin",
    "hospital": "Angelwing Clinic",
    "speciality": "Gynaecology"
},
    {
    "id": 3,
    "name": "Pearl Cruce",
    "hospital": "Little River Hospital",
    "speciality": "Paediatric"
},
    {
    "id": 4,
    "name": "Don Maccament",
    "hospital": "Rosemary Hospital Center",
    "speciality": "Surgery"
},
    {
    "id": 5,
    "name": "Andrew Tessmer",
    "hospital": "Rosemary Hospital Center",
    "speciality": "Gynaecology"
},
    {
    "id": 6,
    "name": "Barrett Cannata",
    "hospital": "Angelwing Clinic",
    "speciality": "Ophthalmology"
},
]

app = Flask(__name__)

@app.route("/doctors")
def get_doctors():
	return doctors

@app.route("/doctors/<category>")
def get_category(category):
	output = []
	for i in range(len(doctors)):
		doctor_dict = doctors[i]
		speciality = doctor_dict.get("speciality")
		if category.casefold() == speciality.casefold():
			output.append(doctor_dict)
	return output

@app.route("/hospitals/<hospital>")
def get_doctors_by_hospital(hospital):
	output = []
	for i in range(len(doctors)):
		doctor_dict = doctors[i]
		hospital_key = doctor_dict.get("hospital")
		if hospital.casefold() == hospital_key.casefold():
			output.append(doctor_dict)
	return output
