import json
import sys

def read_sensitive_fields(file_path):
    sensitive_fields = []
    with open(file_path, 'r') as f:
        for line in f:
            sensitive_fields.append(line.strip())
    return sensitive_fields

def read_json_data(file_path):
    with open(file_path, 'r') as f:
        json_data = json.load(f)
    return json_data

def scrub_value(value):
    if isinstance(value, str) or isinstance(value, int):
        return '*' * len(str(value))
    elif isinstance(value, bool):
        return '-'
    elif isinstance(value, list):
        return [scrub_value(item) for item in value]
    elif isinstance(value, dict):
        return {key: scrub_value(val) for key, val in value.items()}
    else:
        return value

def scrub(json_data, sensitive_fields):
    for field in sensitive_fields:
        if field in json_data:
            json_data[field] = scrub_value(json_data[field])
    return json_data

def write_json_data(json_data, output_file):
    with open(output_file, 'w') as f:
        json.dump(json_data, f, indent=2)
    print(f"Scrubbed data saved to {output_file}")

def main():
    if len(sys.argv) != 4:
        print("Usage: python scrub.py sensitive_fields.txt input.json output.json")
        sys.exit(1)

    sensitive_fields_file = sys.argv[1]
    json_data_file = sys.argv[2]
    output_file = sys.argv[3]

    sensitive_fields = read_sensitive_fields(sensitive_fields_file)
    json_data = read_json_data(json_data_file)
    scrubbed_data = scrub(json_data, sensitive_fields)
    write_json_data(scrubbed_data, output_file)

if __name__ == "__main__":
    main()
