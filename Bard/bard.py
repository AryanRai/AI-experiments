
import bardapi
import os

# set your __Secure-1PSID value to key
os.environ['_BARD_API_KEY']="WQg5a8FOKayi6mwHAJ3GY5Nw-vFvjcw0rYbN6_qwaHtrErj6TIjObOaMO_w4edWsL281uw."

# set your input text
input_name = input("enter your name:")

# Send an API request and get a response.



while True:
    input_text = input(input_name + ": ")
    response = bardapi.core.Bard().get_answer(input_text)
    print("Bard: " + response['content'])