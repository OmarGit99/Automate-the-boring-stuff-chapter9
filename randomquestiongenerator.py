
import random

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany',
   'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

all_states = []
all_capitals = []


for state in capitals:
    all_states.append(state)
    all_capitals.append(capitals[state])

for x in range(50):
    done_questions = []
    fq = open("Capitalquiz"+str(x+1)+".txt", "w")
    fq.write("\nName: \nRoll no.: \nDate: \n")
    fa = open("Capitalquiz"+str(x+1)+"ans.txt", "w")

    for questionno in range(35):
        randindex = random.randint(0,49)

        while(all_states[randindex] in done_questions):
                randindex = random.randint(0,49)

        fq.write("\nQ"+str(questionno+1)+") What is the capital of "+all_states[randindex]+"?\n")
        stateinq = all_states[randindex]


        correctAnswer = capitals[stateinq]
        fa.write("Q"+str(questionno+1)+")Answer: "+correctAnswer+"\n\n")

        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answersoptions = wrongAnswers
        answersoptions.append(correctAnswer)
        random.shuffle(answersoptions)

        for no in range(4):
            number = no+1
            letter = chr(ord('@')+number)
            fq.write("\t"+letter+". "+answersoptions[no]+"\n")

    fq.close()
    fa.close


