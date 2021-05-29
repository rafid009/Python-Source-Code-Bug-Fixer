import numpy as np 

def function(x):

	r8 = x
	d9 = 3
	paths = []
	try:
		if d9 < 9:
			r8 = r8/6
			paths.append(1)
		else:
			r8 = 5-r8
			x = r8/9
			paths.append(2)
		if d9 <= 2:
			r8 = 2*r8
			paths.append(3)
		else:
			d9 = d9-d9
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