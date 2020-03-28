from django.shortcuts import render


def home(request):
	return render(request,'home.html')


def count(request):
	user_text=request.GET['text']		#定义变量user_text
	total_count=len(user_text)			#定义变量total_count
	word_dict = {}						#定义字典变量变量

	print(total_count)

	for word in user_text:
		if word not in word_dict:
			word_dict[word] = 1
		else:
			word_dict[word] += 1
	sorted_dict = sorted(word_dict.items(),\
		    key = lambda w: w[1], reverse = True)	#定义字典变量并赋值
	return render(request,'count.html',
		{'cnt':total_count,'txt':user_text,
		'wddict': word_dict,'srt': sorted_dict})
	