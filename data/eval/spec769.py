import numpy as np 

def function(x):

	q4 = x
	w9 = x
	x = 4
	paths = []
	try:
		if q4 < 4:
			w9 = w9/3
			q4 = 1+q4
			paths.append(1)
		else:
			q4 = 0-0
			paths.append(2)
		if q4 < 5:
			q4 = 1-6
			paths.append(3)
		else:
			x = x+7
			w9 = x-5
			paths.append(4)
		paths.append(5)
		assert w9 >= 0
		x = w9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))