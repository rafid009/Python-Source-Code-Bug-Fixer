import numpy as np 

def function(x):

	f7 = 8
	r0 = x
	paths = []
	try:
		if x <= 2:
			r0 = r0/4
			r0 = r0/2
			paths.append(1)
		else:
			x = 9/r0
			paths.append(2)
		if x >= 2:
			f7 = f7/x
			x = f7-x
			paths.append(3)
		else:
			f7 = 2+f7
			x = f7+2
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