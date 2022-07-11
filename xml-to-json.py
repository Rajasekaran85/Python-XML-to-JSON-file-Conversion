import json
import xmltodict
import os

print("\n Python XML to JSON file conversion \n")
print("\n Application convert the xml files into json files \n")


# pip install xmltodict

filepath1 = input("Enter the path of XML files: ")
filepath = filepath1 + "/"

for fname in os.listdir(filepath):
	if not fname.endswith(".xml"):
		continue
	print(fname)
	xmlfilename1 = filepath + fname
	xmlfilename = open(xmlfilename1, mode="r", encoding="utf8")

	# validating the XML file and reading the content
	xml_parse = xmltodict.parse(xmlfilename.read())
	xmlfilename.close()

	# converting the XML content to JSON structure, indent = use for nested level, ensure_ascii=False for retaining the UTF-8 characters
	conversion = json.dumps(xml_parse, indent=2, ensure_ascii=False)


	# defining the json file name
	split = os.path.splitext(fname)[0]
	print(split)
	json_name = filepath + split + ".json"

	# writing the JSON output
	with open(json_name, mode='w', encoding='utf-8') as json_file:
		json_file.write(conversion)
		json_file.close()
