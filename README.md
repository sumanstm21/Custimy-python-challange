# Custimy-python-challange By Suman Thapa Magar


To run the script:
```
python custimy.py people.json output.json
```
You can run the script with localization
```
python custimy.py people.json output.json --country_id=US
```

Example input:
```
  {
    "email": "colemanwells@custimy-fake.io",
    "name": "Newman"
  },
  ....
```

Example output:
```
  {
    "email": "colemanwells@custimy-fake.io",
    "name": "Newman",
    "age": 52
  },
  ....
```
## Code
The names and emails are first collected from the file and then are send in batch of 10. The api is called two times as the given data is currently 20 records.

The request is async and await because, we are getting request for evey batch and merging the response data in results.

Once we get the result, it is then filtered we save the data in format email, name and age. After it creates the output file.

Finally,
There are arguments you can pass so that it is in the following format 
```
python custimy.py people.json output.json
```
