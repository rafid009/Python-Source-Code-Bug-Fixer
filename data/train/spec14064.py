import numpy as np 

def function(x):

	z6 = 7
	v3 = 8
	paths = []
	try:
		if x <= 7:
			z6 = 3*z6
			z6 = z6+2
			paths.append(1)
		else:
			z6 = 1-z6
			v3 = v3*7
			paths.append(2)
		if z6 > 5:
			v3 = v3-9
			x = x+2
			paths.append(3)
		else:
			v3 = v3*v3
			x = x/x
			v3 = v3*4
			paths.append(4)
		paths.append(5)
		assert v3 >= 0
		x = v3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))