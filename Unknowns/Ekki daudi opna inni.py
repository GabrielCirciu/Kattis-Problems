inputs = [input().split('|') for _ in range(2)]
outputs = []
for i in range(2):
    outputs.append(inputs[0][i]+inputs[1][i])
print(outputs[0]+' '+outputs[1])