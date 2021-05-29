import numpy as np 

def function(x):

	g5 = 3
	w5 = 7
	paths = []
	try:
		if x > 0:
			g5 = g5/9
			g5 = w5-x
			w5 = 7+g5
			paths.append(1)
		else:
			w5 = w5-6
			x = x*5
			paths.append(2)
		if x >= 5:
			w5 = w5*3
			w5 = 0/5
			paths.append(3)
		else:
			g5 = 0/g5
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