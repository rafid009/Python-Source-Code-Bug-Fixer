import numpy as np 

def function(x):

	r1 = 9
	z6 = x
	x = 2
	paths = []
	try:
		if x > 8:
			z6 = x-z6
			paths.append(1)
		else:
			r1 = z6*x
			paths.append(2)
		if r1 <= 0:
			z6 = r1-z6
			paths.append(3)
		else:
			x = x-0
			x = x*1
			paths.append(4)
		paths.append(5)
		assert r1 >= 0
		r1 = r1**0.5
		return r1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))