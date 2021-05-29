import numpy as np 

def function(x):

	k2 = x
	z1 = x
	paths = []
	try:
		if k2 > 9:
			k2 = k2+x
			x = x/6
			paths.append(1)
		else:
			k2 = k2/z1
			x = 0*x
			paths.append(2)
		if x >= 9:
			z1 = z1*2
			x = x+4
			paths.append(3)
		else:
			x = 9/8
			x = x*1
			paths.append(4)
		paths.append(5)
		assert z1 >= 0
		z1 = z1**0.5
		return z1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))