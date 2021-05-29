import numpy as np 

def function(x):

	r1 = x
	r0 = x
	paths = []
	try:
		if r1 > 3:
			x = 9+4
			paths.append(1)
		else:
			r1 = 0+r1
			r0 = r0/3
			paths.append(2)
		if r0 > 9:
			x = 1/x
			x = x*9
			paths.append(3)
		else:
			x = 5+r1
			r1 = r0+3
			r1 = r1/r1
			paths.append(4)
		paths.append(5)
		assert r0 >= 0
		x = r0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))