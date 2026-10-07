import argparse
import os
import json
import tempfile

def load_data(path):
    if not os.path.exists(path):
        return {}
    try:
        with open(path, encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return {} 
    
def write_data(key, val, STORAGE_PATH, BASE_DIR):
    data = load_data(STORAGE_PATH)
    data.setdefault(key, []).append(val)
    with tempfile.NamedTemporaryFile('w', delete=False, encoding='utf-8', dir=BASE_DIR) as tmp:
        json.dump(data, tmp, ensure_ascii=False)

    os.replace(tmp.name, STORAGE_PATH)

def read_data(key, STORAGE_PATH):
    data = load_data(STORAGE_PATH)
    values = data.get(key, [])
    print(', '.join(values))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--key')
    parser.add_argument('--val')
    args = parser.parse_args()

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    STORAGE_PATH = os.path.join(BASE_DIR, 'storage.data')

    if args.val is not None:
        write_data(args.key, args.val, STORAGE_PATH, BASE_DIR)
    else:
        read_data(args.key, STORAGE_PATH)