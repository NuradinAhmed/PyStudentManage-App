student = {
    "Name": "Nuradin",
    "Student_Id": 12345,
    "feedback": None
}
student["last_name"] = "Ifrah"

try:
    last_name = student["last_name"]
    numbered_lastname = last_name + 9#
except KeyError:
    print("Error finding last_name")
except TypeError:
    print("I cant add these two together!")
except Exception:
    print("Unknown error!")

print("This code executes! ")
