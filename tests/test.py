import requests 

json_data = {
  "querry": "string",
  "url":"https://upload.wikimedia.org/wikipedia/commons/1/1b/The_Coleoptera_of_the_British_islands_%28Plate_125%29_%288592917784%29.jpg"
}

sent_url = requests.post("http://127.0.0.1:5000/" , json_data)

print("Printing data")
print(sent_url.text


	