import data_quiz as dq
import data_parse_temp as tmp


def parse_file(filename):
    with open(filename, 'r') as tmp.f:
        dq.quiz_name            = tmp.f.readline().strip()
        dq.number_of_questions  = int(tmp.f.readline())
        dq.number_of_chances    = int(tmp.f.readline())

        for tmp.i in range(dq.number_of_questions):
            tmp.q = {}
            tmp.q['category'] = tmp.f.readline().strip()
            tmp.q['question_text'] = tmp.f.readline().strip()
            tmp.q['choices_count'] = int(tmp.f.readline())
            tmp.q['choices'] = []
            for tmp.j in range(tmp.q['choices_count']):
                tmp.q['choices'].append(tmp.f.readline().strip().lower())
            dq.questions.append(tmp.q)

