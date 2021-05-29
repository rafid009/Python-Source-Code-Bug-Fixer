import numpy as np 

def function(x):

	u6 = 9
	z2 = x
	paths = []
	try:
		if u6 <= 7:
			u6 = u6+4
			paths.append(1)
		else:
			x = 0*8
			x = x*1
			u6 = x*3
			paths.append(2)
		if x >= 0:
			x = z2-8
			paths.append(3)
		else:
			x = 1/x
			z2 = z2-u6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))