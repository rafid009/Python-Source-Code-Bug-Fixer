import numpy as np 

def function(x):

	p9 = x
	w7 = 8
	paths = []
	try:
		if p9 <= 1:
			w7 = x/w7
			paths.append(1)
		else:
			w7 = w7-9
			w7 = 5*5
			w7 = 9-7
			paths.append(2)
		if w7 >= 5:
			x = x+6
			w7 = w7+9
			paths.append(3)
		else:
			x = x-5
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