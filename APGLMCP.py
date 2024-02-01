#!/usr/bin/python3
import random
import json
class flashcards:
    def __init__(self):
        with open('chapter1.txt') as chapter1:
            data = chapter1.read()
        self.terms1 = json.loads(data)
        with open('chapter2.txt') as chapter2:
            data = chapter2.read()
        self.terms2 = json.loads(data)
        with open('chapter3.txt') as chapter3:
            data = chapter3.read()
        self.terms3 = json.loads(data)
        with open('chapter4.txt') as chapter4:
            data = chapter4.read()
        self.terms4 = json.loads(data)
        with open('chapter5.txt') as chapter5:
            data = chapter5.read()
        self.terms5 = json.loads(data)

    def quiz(self):
        choice = int(input("Which Chapter Would You Like to Study? (1/2/3/4/5) \n"))
        if choice == 1:
            terms = self.terms1.items()
        elif choice == 2:
            terms = self.terms2.items()
        elif choice == 3:
            terms = self.terms3.items()
        elif choice == 4:
            terms = self.terms4.items()
        elif choice == 5:
            terms = self.terms5.items()
        previous_choices = []
        while (True):
            term, definition = random.choice(list(terms))
            if term in previous_choices:
                term, definition = random.choice(list(terms))
            else:
                previous_choices.append(term)
                print("{}".format(definition))
                user_answer = input("Enter your Answer: ")
                print("\n Your Answer: " + user_answer.lower())
                print("\n Correct Answer: " + term.lower() + "\n")
            if len(previous_choices) > (len(list(terms))-1 ):
                print("Finished With Chapter " + str(choice) + " Vocabulary! \n")
                fc.quiz()


print("Welcome to AP Gov Last Minute Cram Program (APGLMCP)")
fc = flashcards()
fc.quiz()
