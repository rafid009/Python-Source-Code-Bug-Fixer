import numpy as np 

def function(x):

	o1 = 3
	i1 = x
	paths = []
	try:
		if i1 >= 9:
			o1 = o1*5
			x = 1*x
			i1 = o1/2
			paths.append(1)
		else:
			x = 5-9
			x = 0/x
			o1 = o1/2
			paths.append(2)
		if x <= 8:
			i1 = i1*x
			i1 = 2*x
			o1 = o1/8
			paths.append(3)
		else:
			x = x-o1
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