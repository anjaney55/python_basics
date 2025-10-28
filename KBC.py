questions= [
    ["which language is used youtube?", "Python", "JavaScript", "C", "C++", "c"],
    ["Which is the largest planet in our solar system?", "Earth", "Jupiter", "Mars", "Venus", "b"],
    ["which country is the largest economy in the world?", "India", "China", "USA", "Russia", "c"],
    ["Which is the largest mammal?", "Elephant", "Blue whale", "Giraffe", "Hippopotamus", "b"],
    ["which language is used google?", "Python", "JavaScript", "C", "C++", "b"],
    ["Which is the largest ocean in the world?", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean", "d"],
    ["Which is the largest continent in the world?", "Asia", "Africa", "Europe", "Australia", "a"],
    ["which language is used facebook?", "Python", "JavaScript", "C", "C++", "a"],
    ["Which is the largest desert in the world?", "Sahara Desert", "Arabian Desert", "Gobi Desert", "Kalahari Desert", "a"],
    ["Which is the largest river in the world?", "Amazon River", "Nile River", "Yangtze River", "Mississippi River", "a"],
    ["Which is the largest mountain in the world?", "Mount Everest", "K2", "Kangchenjunga", "Lhotse", "a"],
    ["which language is used instagram?", "Python", "JavaScript", "C", "C++", "b"],
    ["Which is the largest forest in the world?", "Amazon Rainforest", "Taiga", "Congo Rainforest", "Valdivian Temperate Rainforest", "a"],
    ["Which is the largest lake in the world?", "Caspian Sea", "Lake Superior", "Lake Victoria", "Lake Huron", "a"],
    ["which language is used whatsapp?", "Python", "JavaScript", "C", "C++", "a"],
]

levels =[1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 2500000, 5000000, 10000000]
money = 0

for i in range(0, len(questions)):
    question = questions[i]
    print(f"\n\nQustion for Rs.{levels[i]}\n")
    print(f"{question[0]}")
    print(f"a.{question[1]}                 b. {question[2]}")
    print(f"c.{question[3]}                 d. {question[4]}")

    rply = input("Enter your option (a-d) or '0' to quite :\n ")

    if rply==0:
        money=levels[i-1]
        break

    if(rply == question[-1]):
        print(f"Congrats! your answer is correct , you have won Rs.{levels[i]}")
        if(i==4): 
            money=10000
        elif(i==9):
            money=320000
        elif(i==14):
            money=10000000
    else:
        print("Sorry! your answer is wrong")
        break

print(f"\n\nYour total winning prize is Rs.{money}")