import numpy as np 

def function(x):

	w7 = x
	b5 = x
	paths = []
	try:
		if x >= 7:
			w7 = w7+1
			w7 = w7-8
			paths.append(1)
		else:
			b5 = b5*6
			b5 = 2+w7
			paths.append(2)
		if x > 8:
			w7 = 9-w7
			w7 = 0-8
			x = x*2
			paths.append(3)
		else:
			w7 = b5-5
			x = w7/x
			x = b5+x
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