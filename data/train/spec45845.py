import numpy as np 

def function(x):

	d5 = 9
	x9 = x
	paths = []
	try:
		if x >= 3:
			x9 = x9-x9
			x9 = x9*2
			x9 = x9/4
			paths.append(1)
		else:
			x9 = 9*x9
			x9 = x9-2
			d5 = d5/8
			paths.append(2)
		if x9 < 3:
			d5 = d5-6
			d5 = 8-d5
			paths.append(3)
		else:
			d5 = 6*x
			x = x*0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x9 = x**0.5
		return x9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))