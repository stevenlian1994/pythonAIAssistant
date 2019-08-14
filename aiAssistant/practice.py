import wolframalpha
app_id = "49WUTK-JY3L772QUL"
client = wolframalpha.Client(app_id)
my_input = input("Question: ")
res = client.query(my_input)
answer = next(res.results).text 
print(answer)