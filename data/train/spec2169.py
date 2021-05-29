import numpy as np 

def function(x):

	o1 = x
	j5 = 2
	paths = []
	try:
		if x > 0:
			x = o1-6
			j5 = j5-j5
			j5 = 9-j5
			paths.append(1)
		else:
			o1 = 6*6
			paths.append(2)
		if o1 > 2:
			j5 = 9-2
			paths.append(3)
		else:
			j5 = 7/o1
			o1 = o1*9
			x = 4/x
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