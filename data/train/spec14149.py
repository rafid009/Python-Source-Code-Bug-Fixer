import numpy as np 

def function(x):

	b7 = x
	w9 = x
	paths = []
	try:
		if b7 <= 0:
			x = x-4
			x = w9/x
			paths.append(1)
		else:
			x = 5*x
			b7 = b7*7
			paths.append(2)
		if w9 >= 8:
			b7 = b7+7
			paths.append(3)
		else:
			w9 = w9/w9
			x = x/4
			paths.append(4)
		paths.append(5)
		assert b7 >= 0
		b7 = b7**0.5
		return b7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))