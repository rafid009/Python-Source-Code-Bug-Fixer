import numpy as np 

def function(x):

	o1 = x
	j0 = 8
	paths = []
	try:
		if x > 3:
			o1 = o1-x
			j0 = j0+x
			paths.append(1)
		else:
			o1 = 2*o1
			paths.append(2)
		if o1 <= 5:
			x = x-9
			o1 = 2+j0
			paths.append(3)
		else:
			j0 = 8/9
			o1 = 1+o1
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