import numpy as np 

def function(x):

	b6 = 7
	w9 = x
	paths = []
	try:
		if x <= 1:
			w9 = 1-b6
			paths.append(1)
		else:
			b6 = 5*b6
			w9 = 1*w9
			paths.append(2)
		if w9 < 8:
			b6 = b6/b6
			paths.append(3)
		else:
			x = 8+1
			w9 = 0*7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b6 = x**0.5
		return b6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))