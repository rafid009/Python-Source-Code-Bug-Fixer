import numpy as np 

def function(x):

	r1 = 8
	x0 = 1
	x = x
	paths = []
	try:
		if r1 > 9:
			x = 7-4
			x = 6/1
			x = x+4
			paths.append(1)
		else:
			x = x+x0
			x = x/2
			x0 = x0/5
			paths.append(2)
		if r1 < 5:
			r1 = x*4
			paths.append(3)
		else:
			r1 = x0+r1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x0 = x**0.5
		return x0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))