import requests

#GET Request
#response=requests.get("http://216.10.245.166/Library/GetBook.php",params={'ID':'huj878'})
#print(response.text)

url="http://216.10.245.166/Library/Addbook.php"
data = {

"name":"Learn Appium Automation with cherry",
"isbn":"bcd",
"aisle":"6060",
"author":"John cherry"
}


#sending the post request
response=requests.post(url,json=data)


# checking the response
if response.status_code==200:
    print("request was successful")
    print(response.json())

else:
    print(f"request failes with status code {response.status_code}")
    print(response.text)