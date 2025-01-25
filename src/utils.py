import pandas as pd

def save_to_json(data, file_path):
    df = pd.DataFrame(data)
    df.to_json(file_path, orient='records', lines=True)  # save in JSON format
    print(f'Data saved to {file_path}')
