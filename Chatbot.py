print("Select a language to communicate:\nHindi\nEnglish")

n=input("Enter your Name: ")
print("Hello how can I help you today",n,"?")
while True:
    ques=input("what is your query?\n")
    ui=ques.lower()
    if (ques=="hi"):
       print("Hello")
    elif(ui=="where is my order"):
        print("Your order is on the way you can also track your order");
    elif(ui=="can i return" or ui=="i want to return" or  "i want to exchange"):
        print("You can only return till 7 days of delivery")
    elif(ui=="i want to exchange"):
        print("You can exchange it till 7 days of delivery")
    elif(ui=="i want to call customer care service"):
        print("we will connect you with our team , you will get a call back in 5 minutes")
    elif(ui=="can i cancel my order"):
        print("cancellation available till shipping")
    elif(ui=="bye"):
        print("Bye\nBased on communication Rate this conversation from 1 to 10")
        break
    else:
        print("I don't understand") #in case user asks unknown questions like what is ai? or something else
