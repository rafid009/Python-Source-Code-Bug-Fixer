import numpy as np 

def function(x):

	w2 = 4
	q9 = x
	paths = []
	try:
		if w2 >= 8:
			x = x*5
			w2 = 1*2
			w2 = x+w2
			paths.append(1)
		else:
			w2 = w2-x
			w2 = w2-0
			x = x-w2
			paths.append(2)
		if x <= 4:
			q9 = 4*q9
			paths.append(3)
		else:
			q9 = q9*3
			x = x+8
			q9 = x-5
			paths.append(4)
		paths.append(5)
		assert q9 >= 0
		q9 = q9**0.5
		return q9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))