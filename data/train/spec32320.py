import numpy as np 

def function(x):

	a5 = 2
	b5 = 3
	paths = []
	try:
		if a5 > 1:
			a5 = a5+0
			b5 = 6-0
			a5 = 0*2
			paths.append(1)
		else:
			a5 = b5-a5
			b5 = b5-a5
			paths.append(2)
		if x > 5:
			x = x*7
			paths.append(3)
		else:
			b5 = 3*5
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