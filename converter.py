import json
import xml.etree.ElementTree as ET
import argparse
import sys


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
        if len(element) == 0:
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


def handle_conversion(args):
    """
    Handles the conversion based on user-provided arguments.

    Args:
        args (Namespace): Parsed command-line arguments.
    """
    try:
        if args.json_to_xml:
            with open(args.input, "r") as f:
                json_data = json.load(f)
            xml_output = json_to_xml(json_data, root_name=args.root)
            with open(args.output, "w") as f:
                f.write(xml_output)
            print(f"Converted JSON to XML and saved to {args.output}")
        elif args.xml_to_json:
            with open(args.input, "r") as f:
                xml_data = f.read()
            json_output = xml_to_json(xml_data)
            with open(args.output, "w") as f:
                json.dump(json_output, f, indent=4)
            print(f"Converted XML to JSON and saved to {args.output}")
    except Exception as e:
        print(f"Error during conversion: {e}")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description="Convert JSON to XML or XML to JSON.",
        epilog="Example: json-to-xml-converter --json-to-xml --input data.json --output data.xml"
    )
    parser.add_argument("--json-to-xml", action="store_true", help="Convert JSON to XML")
    parser.add_argument("--xml-to-json", action="store_true", help="Convert XML to JSON")
    parser.add_argument("--input", type=str, required=True, help="Input file path")
    parser.add_argument("--output", type=str, required=True, help="Output file path")
    parser.add_argument("--root", type=str, default="root", help="Root element name for XML")
    parser.add_argument("--version", action="version", version="json-to-xml-converter 1.0.0")
    args = parser.parse_args()

    if not (args.json_to_xml or args.xml_to_json):
        parser.print_help()
        sys.exit(1)

    handle_conversion(args)


if __name__ == "__main__":
    # main()

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
