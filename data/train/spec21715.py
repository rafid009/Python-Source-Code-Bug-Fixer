import numpy as np 

def function(x):

	z9 = x
	o3 = x
	paths = []
	try:
		if o3 < 6:
			o3 = z9-6
			paths.append(1)
		else:
			x = 4/x
			o3 = o3+x
			paths.append(2)
		if x >= 5:
			z9 = o3*7
			paths.append(3)
		else:
			x = x*4
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