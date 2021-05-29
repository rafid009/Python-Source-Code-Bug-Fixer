import numpy as np 

def function(x):

	r0 = 7
	n5 = x
	paths = []
	try:
		if r0 > 7:
			x = n5*x
			n5 = n5/9
			paths.append(1)
		else:
			x = x/7
			paths.append(2)
		if n5 > 4:
			x = 4-x
			paths.append(3)
		else:
			n5 = n5+2
			n5 = n5+n5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r0 = x**0.5
		return r0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))