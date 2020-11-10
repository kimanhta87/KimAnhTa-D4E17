quiz = {
    'question' : 'con cho co may chan',
    'answer' : '3',
    'choice' : '1,2,3,4',

}


print(quiz['question'])
print(quiz['choice'])

user_answer = input('your answer:')

if user_answer == quiz['answer']:
    print('you are correct')

else:
    print('wrong')





