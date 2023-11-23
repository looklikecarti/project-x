#1
import re
def check_license_plate(plate):
    private_car_pattern = re.compile(r'^[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}$')
    taxi_pattern = re.compile(r'^[АВЕКМНОРСТУХ]{2}\d{3}\d{2,3}$')
    if private_car_pattern.match(plate):
        return "Частный легковой автомобиль"
    elif taxi_pattern.match(plate):
        return "Такси"
    else:
        return "Некорректный номер"
plate_number = "А123ВС45"
result = check_license_plate(plate_number)
print(result)


#2
word_count = sum(1 for line in open('your_file.txt') for word in line.split('-') if word.isalpha())
print(word_count)


#3
import re
def replace_time_with_tbd(text):
    time_pattern = re.compile(r'\b\d{2}:\d{2}(:\d{2})?\b')
    result = time_pattern.sub('(TBD)', text)
    return result
input_text = "Уважаемые! Если вы к 09:00 не вернёте чемодан, то уже в 09:00:01 я за себя не отвечаю."
output_text = replace_time_with_tbd(input_text)
print(output_text)


#4
import re
def extract_abbreviations(text):
    abbreviation_pattern = re.compile(r'\b[A-Z]{2,}\b')
    abbreviations = abbreviation_pattern.findall(text)
    return abbreviations
input_text = "ФГУП НИЦ ГИДГЕО, ФГОУ ЧШУ АПК и т.п."
result = extract_abbreviations(input_text)
print(result)
