import numpy as np 

def function(x):

	v0 = 5
	z9 = 9
	paths = []
	try:
		if z9 > 5:
			x = x-5
			x = 1*x
			paths.append(1)
		else:
			z9 = z9*1
			paths.append(2)
		if z9 > 8:
			v0 = x-2
			z9 = 6*z9
			paths.append(3)
		else:
			x = z9-0
			x = v0+x
			x = v0+4
			paths.append(4)
		paths.append(5)
		assert v0 >= 0
		v0 = v0**0.5
		return v0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))