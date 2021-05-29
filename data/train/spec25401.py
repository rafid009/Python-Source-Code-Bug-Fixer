import numpy as np 

def function(x):

	y7 = 8
	r0 = 7
	paths = []
	try:
		if y7 < 8:
			x = x-4
			y7 = 6+y7
			r0 = r0*9
			paths.append(1)
		else:
			y7 = 6/y7
			x = x-5
			paths.append(2)
		if x > 5:
			r0 = r0*y7
			r0 = 1-r0
			paths.append(3)
		else:
			y7 = y7-x
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