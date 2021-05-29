import numpy as np 

def function(x):

	v8 = x
	z0 = 6
	paths = []
	try:
		if z0 > 7:
			x = 8-x
			paths.append(1)
		else:
			v8 = 1+v8
			z0 = z0+x
			x = 1*z0
			paths.append(2)
		if x > 4:
			z0 = z0/7
			paths.append(3)
		else:
			x = x/v8
			x = 4-1
			v8 = v8-6
			paths.append(4)
		paths.append(5)
		assert v8 >= 0
		x = v8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))