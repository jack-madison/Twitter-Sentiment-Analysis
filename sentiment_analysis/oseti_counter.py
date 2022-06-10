results = [{'positive': 2, 'negative': 1}, {'positive': 1, 'negative': 0}, {'positive': 4, 'negative': 2}, {'positive': 1, 'negative': 3}, {'positive': 2, 'negative': 1}]

positive = 0
negative = 0

for result in results:
    positive = positive + result['positive']
    negative = negative + result['negative']

print('There were ' + str(positive) + ' positive keywords')
print('There were ' + str(negative) + ' negative keywords')