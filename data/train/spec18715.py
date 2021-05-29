import numpy as np 

def function(x):

	z1 = 8
	r5 = 5
	paths = []
	try:
		if x <= 6:
			z1 = z1*1
			z1 = 9/x
			paths.append(1)
		else:
			z1 = z1-z1
			paths.append(2)
		if r5 >= 0:
			r5 = z1*r5
			x = 2*2
			x = x+8
			paths.append(3)
		else:
			x = x/x
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