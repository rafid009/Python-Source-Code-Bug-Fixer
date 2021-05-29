import numpy as np 

def function(x):

	r6 = 7
	z7 = 5
	paths = []
	try:
		if x < 0:
			z7 = r6*9
			x = x+5
			paths.append(1)
		else:
			r6 = r6+z7
			paths.append(2)
		if z7 > 9:
			r6 = 2-3
			paths.append(3)
		else:
			x = 7+r6
			x = 2*x
			paths.append(4)
		paths.append(5)
		assert r6 >= 0
		x = r6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))