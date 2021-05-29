import numpy as np 

def function(x):

	o2 = x
	z1 = x
	paths = []
	try:
		if x > 5:
			z1 = z1+z1
			x = o2-o2
			o2 = o2*z1
			paths.append(1)
		else:
			x = x*6
			paths.append(2)
		if z1 >= 7:
			x = 2+x
			z1 = z1+3
			z1 = 5*z1
			paths.append(3)
		else:
			z1 = z1/7
			paths.append(4)
		paths.append(5)
		assert o2 >= 0
		o2 = o2**0.5
		return o2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))