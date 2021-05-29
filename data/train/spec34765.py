import numpy as np 

def function(x):

	r7 = x
	z7 = 1
	paths = []
	try:
		if x <= 3:
			x = x+8
			x = x-r7
			paths.append(1)
		else:
			x = 1+x
			r7 = z7*5
			r7 = r7*x
			paths.append(2)
		if r7 > 0:
			r7 = 7+r7
			z7 = 7/4
			r7 = 3/r7
			paths.append(3)
		else:
			x = x+9
			paths.append(4)
		paths.append(5)
		assert r7 >= 0
		z7 = r7**0.5
		return z7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))