import numpy as np 

def function(x):

	z1 = 7
	o2 = x
	paths = []
	try:
		if o2 > 8:
			o2 = o2*7
			x = o2-o2
			paths.append(1)
		else:
			o2 = o2-9
			x = 1/6
			z1 = 7*z1
			paths.append(2)
		if x >= 1:
			o2 = x*o2
			x = o2-z1
			paths.append(3)
		else:
			x = 8/2
			o2 = o2+6
			paths.append(4)
		paths.append(5)
		assert o2 >= 0
		x = o2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))