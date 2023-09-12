import numpy as np

def calculate_frequency(key_numbers):
    return (2 ** ((key_numbers - 49) / 12)) * 440

def create_piano_table(model_name, num_keys):
    key_numbers = np.arange(1, num_keys + 1)
    frequencies = calculate_frequency(key_numbers)
    return np.column_stack((key_numbers, frequencies))

# Define the models and their number of keys
models = {
    "CTK-2550": 61,
    "CTK-3500": 61,
    "CTK-6250": 76
}

# Create and print the frequency tables for each model
for model, num_keys in models.items():
    frequency_table = create_piano_table(model, num_keys)
    print(f"{model} Piano Frequency Table:")
    print("Key Number | Frequency (Hz)")
    print("---------------------------")
    for key, frequency in frequency_table:
        print(f"{int(key):10} | {frequency:.2f}")
    print("\n")
