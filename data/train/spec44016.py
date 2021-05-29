import numpy as np 

def function(x):

	x3 = 5
	b9 = 7
	paths = []
	try:
		if x < 1:
			x = x+2
			paths.append(1)
		else:
			b9 = 8/9
			x = x3-x
			paths.append(2)
		if x >= 4:
			x = x*2
			x3 = x3*6
			paths.append(3)
		else:
			b9 = 1+5
			x = x-4
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