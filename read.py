data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line.strip())
		count += 1
		if count % 1000 ==0:
			print(len(data))
print('檔案讀取玩了,總共有', len(data),'比資料')
sum_len = 0
for d in data:
	sum_len = sum_len +len(d)
print('留言的平均長度爲', sum_len/len(data))