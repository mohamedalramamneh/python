def convert_indian_to_arabic(indian_number):
    # خريطة التحويل من الأرقام الهندية إلى الأرقام العربية
    indian_to_arabic = {
        '٠': '0', '١': '1', '٢': '2', '٣': '3', '٤': '4',
        '٥': '5', '٦': '6', '٧': '7', '٨': '8', '٩': '9'
    }

    arabic_number = ""
    for ch in indian_number:
        # إذا كان الحرف رقم هندي يتم تحويله، وإذا لا يُترك كما هو (مثل الفراغ)
        arabic_number += indian_to_arabic.get(ch, ch)
    
    return arabic_number

# مثال على الاستخدام:
input_number = "٣ ٢"
output_number = convert_indian_to_arabic(input_number)
print("النتيجة:", output_number)
