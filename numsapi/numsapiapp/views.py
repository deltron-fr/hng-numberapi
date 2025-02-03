from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import NumberSerializer
import requests

def is_prime(number):
    if number <= 1:
        return False
    else:
        for i in range(2, number):
            if number % i == 0:
                return False
        return True
    
def is_perfect(number):
    if number <= 0:
        return False
    divisors_sum = sum([i for i in range(1, number) if number % i == 0])
    return divisors_sum == number

def get_properties(number):
    power = len(str(number))
    sum_of_digits = 0
    if number >= 0:
        for i in str(number):
            if i != ".":
                sum_of_digits += int(i)**power
        if sum_of_digits == number and (number % 2 == 0):
            return ["armstrong", "even"]
        elif sum_of_digits == number and (number % 2 != 0):
            return ["armstrong", "odd"]
        elif sum_of_digits != number and (number % 2 == 0):
            return ["even"]
        else:
            return ["odd"]
    else:
        return ["even"] if number % 2 == 0 else ["odd"]

def digit_sum(number):
    return sum(int(digit) for digit in str(abs(int(number))))

def get_fun_fact(number):
    api_url = f"http://numbersapi.com/{int(number)}/math"
    try:
        response = requests.get(api_url, timeout=5)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:  
        return f"No fun fact available for {number}."


@api_view(['GET'])
def classify_number(request):
    number_str = request.GET.get("number")
    
    try:
        number = float(number_str)
    except ValueError:
        return Response({"number":number_str, "error": True}, status=status.HTTP_400_BAD_REQUEST)
        
    prime = is_prime(int(number)) 
    perfect = is_perfect(int(number)) 
    properties = get_properties(number)
    sum_of_digits = digit_sum(int(abs(number)))
    fun_fact = get_fun_fact(number)

    data = {
        "number": number,
        "is_prime": prime,
        "is_perfect": perfect,
        "properties": properties,
        "digit_sum": sum_of_digits,
        "fun_fact": fun_fact
    }

    serializer = NumberSerializer(data=data)
    if serializer.is_valid():
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





