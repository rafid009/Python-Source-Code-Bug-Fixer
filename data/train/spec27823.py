import numpy as np 

def function(x):

	r5 = x
	z8 = 5
	paths = []
	try:
		if x <= 4:
			x = 7/6
			z8 = 6+0
			paths.append(1)
		else:
			z8 = 2+z8
			x = r5*z8
			r5 = 8-9
			paths.append(2)
		if z8 < 7:
			x = x*x
			r5 = r5/4
			paths.append(3)
		else:
			r5 = 4-6
			r5 = r5*6
			r5 = 3-r5
			paths.append(4)
		paths.append(5)
		assert r5 >= 0
		x = r5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))