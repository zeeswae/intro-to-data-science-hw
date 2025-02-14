def typeBasedTransformer(**kwargs):
    result = {}
    for i, value in kwargs.items():
        if isinstance(value, (int, float)):
            result[i] = value ** 2  
        elif isinstance(value, str):
            result[i] = value[::-1]  
        elif isinstance(value, bool):
            result[i] = not value  
        elif isinstance(value, (list, tuple)):
            result[i] = value[::-1]  
        elif isinstance(value, dict):
            if len(value.values()) == len(set(value.values())):
                result[i] = {v: k for k, v in value.items()}
            else:
                result[i] = value
        else:
            result[i] = value
    
    return result
data_sample = {
    "integer": 4,
    "floating": 2.5,
    "word": "Hello",
    "boolean": True,
    "list_example": [1, 2, 3],
    "tuple_example": ("a", "b", "c"),
    "dictionary": {"x": 1, "y": 2},
    "other": {1, 2, 3}
}
transformed_data = typeBasedTransformer(**data_sample)
print(transformed_data)
