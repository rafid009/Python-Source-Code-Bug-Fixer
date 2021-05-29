import numpy as np 

def function(x):

	r3 = 5
	a4 = 2
	paths = []
	try:
		if x < 2:
			r3 = r3-a4
			a4 = 9-9
			paths.append(1)
		else:
			a4 = a4*8
			x = x-x
			r3 = 5-r3
			paths.append(2)
		if x <= 8:
			a4 = a4+a4
			paths.append(3)
		else:
			x = r3*x
			x = x-5
			r3 = r3*2
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