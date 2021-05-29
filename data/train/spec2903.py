import numpy as np 

def function(x):

	w9 = x
	q5 = 3
	paths = []
	try:
		if w9 > 3:
			q5 = q5/8
			w9 = 9*w9
			paths.append(1)
		else:
			w9 = 6-0
			w9 = 5*2
			w9 = w9*1
			paths.append(2)
		if x <= 2:
			w9 = w9-4
			w9 = w9/x
			paths.append(3)
		else:
			q5 = q5+2
			w9 = w9*w9
			q5 = q5-0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q5 = x**0.5
		return q5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))