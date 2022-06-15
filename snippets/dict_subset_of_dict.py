marks ={
	'Dan': 85,
	'paul': 73,
	'rashid': 89,
	'potter': 94,
	'avi': 82
}

# make a dict of all marks over 80

marks_over_80 = {key:val for key, val in marks.items() if val > 80}

print(marks_over_80)

