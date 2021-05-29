import numpy as np 

def function(x):

	r9 = 1
	r0 = 6
	paths = []
	try:
		if r0 >= 0:
			r9 = r0-7
			x = 1*x
			paths.append(1)
		else:
			r9 = x-5
			x = 7/x
			r0 = r0+r9
			paths.append(2)
		if r0 < 8:
			x = r0/x
			paths.append(3)
		else:
			r9 = 9*r9
			x = x-r9
			paths.append(4)
		paths.append(5)
		assert r9 >= 0
		x = r9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))