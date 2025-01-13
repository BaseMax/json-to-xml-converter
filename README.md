# JSON to XML Converter

`json-to-xml-converter` is a simple Python library for converting JSON data to XML and vice versa. It allows you to easily convert JSON files to XML format or XML files to JSON format using command-line arguments.

## Features
- Converts JSON to XML with customizable root element.
- Converts XML to JSON while handling nested elements and arrays.
- Command-line utility for easy conversion of files.
- Supports both Python scripts and command-line execution.

## Installation

To use `json-to-xml-converter`, you need Python 3 installed. Clone this repository to your local machine:

```bash
git clone https://github.com/BaseMax/json-to-xml-converter.git
cd json-to-xml-converter
```

### Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Command-Line Usage

You can run the converter directly from the command line:

```bash
python converter.py --json-to-xml --input input.json --output output.xml
```

This converts a JSON file to XML. To convert XML to JSON, use:

```bash
python converter.py --xml-to-json --input input.xml --output output.json
```

#### Options:
- `--json-to-xml`: Convert JSON to XML.
- `--xml-to-json`: Convert XML to JSON.
- `--input`: Path to the input file (either `.json` or `.xml`).
- `--output`: Path to the output file (either `.xml` or `.json`).
- `--root`: Name of the root element for XML (optional, default is "root").
- `--version`: Display the version of the converter.

### Example Usage in Python

You can also import the library functions directly into your Python code for more control over the conversion:

```python
import json
from converter import json_to_xml, xml_to_json

# Example JSON to XML conversion
json_data = {
    "person": {
        "name": "John Doe",
        "age": 30,
        "hobbies": ["reading", "cycling", "hiking"]
    }
}
xml_output = json_to_xml(json_data, root_name="data")
print("XML Output:
", xml_output)

# Example XML to JSON conversion
xml_data = '''
<data>
    <person>
        <name>John Doe</name>
        <age>30</age>
        <hobbies>
            <item>reading</item>
            <item>cycling</item>
            <item>hiking</item>
        </hobbies>
    </person>
</data>
'''
json_output = xml_to_json(xml_data)
print("
JSON Output:
", json.dumps(json_output, indent=4))
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributions

Feel free to fork, submit issues, and create pull requests. Contributions are welcome!

## Copyright

2025 Max Base

