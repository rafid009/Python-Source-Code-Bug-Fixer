import numpy as np 

def function(x):

	w9 = 8
	b6 = 8
	paths = []
	try:
		if x < 5:
			w9 = 9-w9
			b6 = 6+b6
			paths.append(1)
		else:
			x = x*5
			paths.append(2)
		if w9 >= 6:
			x = 6-6
			w9 = w9*w9
			paths.append(3)
		else:
			x = x+4
			w9 = 4-9
			b6 = x*7
			paths.append(4)
		paths.append(5)
		assert b6 >= 0
		x = b6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))