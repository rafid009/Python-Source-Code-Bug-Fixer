import numpy as np 

def function(x):

	f0 = x
	q7 = x
	paths = []
	try:
		if f0 <= 5:
			f0 = f0+q7
			f0 = x-8
			paths.append(1)
		else:
			x = 2*x
			q7 = 2/7
			q7 = 2/q7
			paths.append(2)
		if f0 > 7:
			f0 = 7-f0
			paths.append(3)
		else:
			f0 = f0-q7
			q7 = 4+6
			x = 5*x
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