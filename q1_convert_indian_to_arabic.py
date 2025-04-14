def convert_indian_to_arabic(indian_number):
    # Mapping from Indian numerals to Arabic numerals
    indian_to_arabic = {
        '٠': '0', '١': '1', '٢': '2', '٣': '3', '٤': '4',
        '٥': '5', '٦': '6', '٧': '7', '٨': '8', '٩': '9'
    }

    arabic_number = ""
    for ch in indian_number:
        # Convert if it's an Indian numeral, otherwise keep as is (e.g., space)
        arabic_number += indian_to_arabic.get(ch, ch)
    
    return arabic_number

# Example usage:
input_number = "٣ ٢"
output_number = convert_indian_to_arabic(input_number)
print("Result:", output_number)
