import numpy as np 

def function(x):

	p7 = 3
	w4 = 4
	paths = []
	try:
		if p7 > 0:
			w4 = 7/3
			x = x-1
			paths.append(1)
		else:
			x = x/w4
			paths.append(2)
		if x > 7:
			w4 = w4/1
			paths.append(3)
		else:
			p7 = p7+p7
			x = p7*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w4 = x**0.5
		return w4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))