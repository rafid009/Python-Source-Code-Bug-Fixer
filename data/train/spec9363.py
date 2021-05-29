import numpy as np 

def function(x):

	l3 = 2
	r2 = x
	paths = []
	try:
		if r2 <= 4:
			x = x-5
			paths.append(1)
		else:
			r2 = 9*0
			x = x+r2
			paths.append(2)
		if r2 <= 5:
			x = x-2
			paths.append(3)
		else:
			l3 = x-1
			x = l3-2
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