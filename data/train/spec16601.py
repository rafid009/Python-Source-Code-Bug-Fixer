import numpy as np 

def function(x):

	z7 = x
	r6 = 6
	x = x
	paths = []
	try:
		if z7 > 6:
			x = x+x
			r6 = r6+3
			paths.append(1)
		else:
			x = 6*r6
			paths.append(2)
		if r6 > 8:
			x = x*z7
			z7 = 4*1
			x = 5-x
			paths.append(3)
		else:
			x = x+x
			x = 3-x
			r6 = 8/4
			paths.append(4)
		paths.append(5)
		assert z7 >= 0
		x = z7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))