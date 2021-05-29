import numpy as np 

def function(x):

	l7 = 1
	w9 = x
	paths = []
	try:
		if x > 3:
			w9 = 5*2
			x = x+l7
			x = 1+x
			paths.append(1)
		else:
			l7 = 0*5
			w9 = x+x
			w9 = w9*5
			paths.append(2)
		if l7 <= 6:
			l7 = l7+3
			paths.append(3)
		else:
			l7 = l7-w9
			w9 = w9-w9
			x = w9-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))