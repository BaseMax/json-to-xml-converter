import json
from converter import json_to_xml, xml_to_json

if __name__ == "__main__":
    json_data = {
        "person": {
            "name": "John Doe",
            "age": 30,
            "hobbies": ["reading", "cycling", "hiking"]
        }
    }
    xml_output = json_to_xml(json_data, root_name="data")
    print("XML Output:\n", xml_output)

    xml_data = """
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
    """
    json_output = xml_to_json(xml_data)
    print("\nJSON Output:\n", json.dumps(json_output, indent=4))
