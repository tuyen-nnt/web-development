import pyttsx3
def speak(text):
    # text = "The outbreak is so widespread that 18 states have been placed in a so-called red zone because they have more than 100 new cases per 100,000 people per week, according to an unpublished report distributed this week by the White House coronavirus task force, which urged many states to take stricter steps to contain the spread."
    engine = pyttsx3.init()
    engine.say(str(text))
    engine.runAndWait()