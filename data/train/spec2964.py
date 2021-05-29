import numpy as np 

def function(x):

	z7 = 5
	r9 = x
	x = x
	paths = []
	try:
		if z7 > 0:
			x = 0/2
			z7 = 3-z7
			r9 = r9/7
			paths.append(1)
		else:
			r9 = r9-5
			paths.append(2)
		if z7 < 6:
			r9 = 5-8
			z7 = 5*8
			paths.append(3)
		else:
			x = x/x
			x = x+1
			x = 2*x
			paths.append(4)
		paths.append(5)
		assert r9 >= 0
		r9 = r9**0.5
		return r9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))