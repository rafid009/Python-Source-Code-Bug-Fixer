import numpy as np 

def function(x):

	q7 = x
	w5 = 8
	x = x
	paths = []
	try:
		if w5 > 1:
			q7 = q7+q7
			paths.append(1)
		else:
			w5 = 7/q7
			paths.append(2)
		if x >= 6:
			w5 = x/x
			w5 = w5-7
			q7 = q7-5
			paths.append(3)
		else:
			w5 = 4/x
			w5 = 7+3
			x = x+1
			paths.append(4)
		paths.append(5)
		assert q7 >= 0
		q7 = q7**0.5
		return q7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))