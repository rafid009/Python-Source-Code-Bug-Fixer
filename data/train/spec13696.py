import numpy as np 

def function(x):

	w9 = x
	q4 = 6
	paths = []
	try:
		if w9 < 9:
			w9 = w9+7
			x = 0*x
			q4 = q4/2
			paths.append(1)
		else:
			w9 = x/2
			paths.append(2)
		if w9 < 1:
			x = 1*q4
			x = x-1
			paths.append(3)
		else:
			w9 = 4/7
			x = x+7
			q4 = q4-4
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