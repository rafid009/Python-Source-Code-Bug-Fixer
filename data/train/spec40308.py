import numpy as np 

def function(x):

	r4 = x
	z4 = x
	paths = []
	try:
		if z4 >= 3:
			z4 = 5+x
			paths.append(1)
		else:
			r4 = r4+0
			r4 = x+1
			paths.append(2)
		if r4 < 5:
			x = 3/x
			paths.append(3)
		else:
			z4 = r4+z4
			r4 = r4+4
			r4 = r4*1
			paths.append(4)
		paths.append(5)
		assert r4 >= 0
		r4 = r4**0.5
		return r4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))