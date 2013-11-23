import data_quiz as dq
import data_run_temp as drt
import data_status as ds
import process_parse_file as ppf
import process_display_results as pdr


def run_game():
    """Run the game program."""
    ppf.parse_file("text_game.txt")
    display_welcome_message()
    while (ds.chances_taken < dq.number_of_chances) and (len(ds.correctly_answered) < dq.number_of_questions):
        if drt.current_question not in ds.correctly_answered:
            ask_question()
        drt.current_question += 1
        drt.current_question %= dq.number_of_questions
    pdr.display_summary()


def ask_question():
    """Prompt user for a response to the current question. Determine if they are correct or not."""
    print "Category: %s" % (dq.questions[drt.current_question]['category'])
    print "Question: %s" % (dq.questions[drt.current_question]['question_text'])
    drt.user_response = raw_input("Answer: ").lower()
    if drt.user_response in dq.questions[drt.current_question]['choices']:
        print "Correct!"
        ds.correctly_answered.append(drt.current_question)
    else:
        print "Incorrect"
    ds.chances_taken += 1


def display_welcome_message():
    """Display a welcome message for the game."""
    print "Hello, welcome to the %s game." % dq.quiz_name
    print "You will be given up to %d chances to answer %d questions." % (dq.number_of_chances, dq.number_of_questions)


if "__main__" == __name__:
    run_game()

