import numpy as np 

def function(x):

	v0 = 5
	n5 = 8
	x = 6
	paths = []
	try:
		if v0 > 4:
			x = x*9
			n5 = n5/8
			x = 3-x
			paths.append(1)
		else:
			n5 = 4+n5
			n5 = n5/2
			x = x-4
			paths.append(2)
		if x > 8:
			x = 5/x
			n5 = n5-3
			n5 = n5+1
			paths.append(3)
		else:
			v0 = v0-3
			v0 = v0-5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v0 = x**0.5
		return v0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))