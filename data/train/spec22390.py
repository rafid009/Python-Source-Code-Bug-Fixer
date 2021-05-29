import numpy as np 

def function(x):

	r6 = x
	z4 = 1
	paths = []
	try:
		if r6 < 9:
			x = r6-z4
			r6 = 7-r6
			paths.append(1)
		else:
			x = x+4
			paths.append(2)
		if r6 >= 7:
			z4 = z4*5
			x = x/9
			r6 = 4*1
			paths.append(3)
		else:
			z4 = z4+z4
			paths.append(4)
		paths.append(5)
		assert r6 >= 0
		r6 = r6**0.5
		return r6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))