import json
import xml.etree.ElementTree as ET


def json_to_xml(json_data, root_name="root"):
    """
    Converts JSON data to XML format.

    Args:
        json_data (dict): JSON data to convert.
        root_name (str): Name of the root element.

    Returns:
        str: XML string representation.
    """
    def build_xml_element(parent, data):
        if isinstance(data, dict):
            for key, value in data.items():
                child = ET.SubElement(parent, key)
                build_xml_element(child, value)
        elif isinstance(data, list):
            for item in data:
                item_element = ET.SubElement(parent, "item")
                build_xml_element(item_element, item)
        else:
            parent.text = str(data)

    root = ET.Element(root_name)
    build_xml_element(root, json_data)
    return ET.tostring(root, encoding="unicode")


def xml_to_json(xml_data):
    """
    Converts XML data to JSON format.

    Args:
        xml_data (str): XML string to convert.

    Returns:
        dict: JSON representation.
    """
    def parse_element(element):
        if not element:
            return element.text
        result = {}
        for child in element:
            child_result = parse_element(child)
            tag = child.tag
            if tag in result:
                if not isinstance(result[tag], list):
                    result[tag] = [result[tag]]
                result[tag].append(child_result)
            else:
                result[tag] = child_result
        return result

    root = ET.fromstring(xml_data)
    return {root.tag: parse_element(root)}


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
