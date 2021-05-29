import numpy as np 

def function(x):

	l8 = x
	h8 = 1
	paths = []
	try:
		if x <= 4:
			l8 = l8/l8
			x = x+9
			l8 = x*2
			paths.append(1)
		else:
			l8 = l8*x
			h8 = 6*l8
			paths.append(2)
		if l8 >= 7:
			x = x-7
			l8 = l8-0
			paths.append(3)
		else:
			x = 5-h8
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