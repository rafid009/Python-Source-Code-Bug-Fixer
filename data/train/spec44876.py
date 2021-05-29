import numpy as np 

def function(x):

	o5 = x
	z9 = x
	paths = []
	try:
		if o5 > 4:
			x = 5-6
			z9 = z9*8
			o5 = 5*8
			paths.append(1)
		else:
			o5 = 4-x
			o5 = 3*o5
			z9 = 4*z9
			paths.append(2)
		if x >= 7:
			x = 1/x
			paths.append(3)
		else:
			x = 7/4
			paths.append(4)
		paths.append(5)
		assert z9 >= 0
		x = z9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))