def break_data_into_rows(data):
    if isinstance(data, str):
        return data.split('\n')
    return [line.replace('\n', '') for line in data]