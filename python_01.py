import re
import random
import numpy as np

source = 'english_words_01.txt'
n_tests = 50
n_questions = 50

def create_words_dict(source):
    with open(source) as f:
        data = f.read()

    english_words = re.findall('[a-z-]+', data)
    ja = re.findall('\s.*\n', data)

    meanings = []
    for word in ja:
        m = re.sub('\t|\n', '', word)
        meanings.append(m)

    words_dict = dict(zip(english_words, meanings))
    
    return english_words, meanings, words_dict


if __name__ == '__main__':
    english_words, meanings, words_dict = create_words_dict(source)

    for test_num in range(n_tests):
        with open('英単語テスト_{:02d}.txt'.format(test_num + 1), 'w') as f:

            f.write('出席番号:\n'
                    '名前:\n\n'
                    f'第{test_num + 1}回 単語テスト\n\n')

            random_index = np.random.randint(low=0, high=len(english_words), size=n_questions)

            for question_num in range(n_questions):
                question_word = english_words[random_index[question_num]]
                correct_answer = words_dict[question_word]

                meanings_copy = meanings.copy()
                meanings_copy.remove(correct_answer)
                wrong_answers = random.sample(meanings_copy, 3)

                answer_options = [correct_answer] + wrong_answers

                random.shuffle(answer_options)

                f.write(f'問{question_num + 1}. {question_word}\n\n')

                for i in range(4):
                    f.write(f'{i + 1}. {answer_options[i]}\n')
                f.write('\n\n')