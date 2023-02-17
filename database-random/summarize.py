import csv
import os
import regex


ALL_SUBCATEGORIES = ['American Literature', 'British Literature', 'Classical Literature', 'European Literature', 'World Literature', 'Other Literature', 'American History', 'Ancient History', 'European History', 'World History', 'Other History',
                     'Biology', 'Chemistry', 'Physics', 'Math', 'Other Science', 'Visual Fine Arts', 'Auditory Fine Arts', 'Other Fine Arts', 'Religion', 'Mythology', 'Philosophy', 'Social Science', 'Current Events', 'Geography', 'Other Academic', 'Trash']

ALL_DIFFICULTIES = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

LOGS_DIRECTORY = 'logs'

QUESTION_TYPES = ['tossup', 'bonus', 'all']

stats = {
    question_type: [[0 for _ in ALL_DIFFICULTIES] for _ in ALL_SUBCATEGORIES] for question_type in QUESTION_TYPES
}

skipped_count = 0

for file in os.listdir(LOGS_DIRECTORY):
    f = open(f'{LOGS_DIRECTORY}/{file}', 'r', encoding='utf-8-sig')

    for line in f:
        line = line.strip()

        if line in ['"message"', '']:
            continue

        try:
            subcategories = regex.findall(r'(?<=subcategories: \\u001b\[92m).*?(?=\\)', line)[0]
            subcategories = subcategories.split(',')

            difficulties = regex.findall(r'(?<=difficulties: \\u001b\[92m).*?(?=\\)', line)[0]
            difficulties = [int(difficulty) for difficulty in difficulties.split(',')]
        except:
            print(line)
            continue

        if sorted(subcategories) == sorted(ALL_SUBCATEGORIES) and sorted(difficulties) == sorted(ALL_DIFFICULTIES):
            skipped_count += 1
            continue

        question_type = regex.findall(r'(?<=question type: \\u001b\[92m).*?(?=\\)', line)[0]

        for subcategory in subcategories:
            for difficulty in difficulties:
                if difficulty not in ALL_DIFFICULTIES:
                    continue

                subcategory_index = ALL_SUBCATEGORIES.index(subcategory)
                difficulty_index = ALL_DIFFICULTIES.index(difficulty)
                stats[question_type][subcategory_index][difficulty_index] += 1
                stats['all'][subcategory_index][difficulty_index] += 1

difficulty_totals = {
    question_type: [
        sum([
            stats[question_type][i][j] for i in range(len(ALL_SUBCATEGORIES))
        ]) for j in range(len(ALL_DIFFICULTIES))
    ] for question_type in stats
}

for question_type in ['all']:
    h = open(f'summary-{question_type}.csv', 'w')
    writer = csv.writer(h)
    writer.writerow([''] + ALL_DIFFICULTIES + ['Totals:'])

    for i, subcategory in enumerate(ALL_SUBCATEGORIES):
        writer.writerow([subcategory] + stats[question_type][i] + [sum(stats[question_type][i])])

    writer.writerow(['Totals:'] + difficulty_totals[question_type] + [sum(difficulty_totals[question_type])])

print(f'Skipped {skipped_count} lines')
