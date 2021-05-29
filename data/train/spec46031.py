import numpy as np 

def function(x):

	a7 = 6
	r4 = 4
	paths = []
	try:
		if x > 4:
			x = 3+4
			paths.append(1)
		else:
			r4 = r4-a7
			paths.append(2)
		if r4 <= 7:
			r4 = 4-9
			r4 = r4-8
			a7 = 3+a7
			paths.append(3)
		else:
			a7 = a7-9
			r4 = r4*7
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