import numpy as np 

def function(x):

	r8 = 4
	x4 = 4
	paths = []
	try:
		if x4 >= 5:
			x = x+x
			r8 = r8-r8
			paths.append(1)
		else:
			x4 = 3-6
			paths.append(2)
		if r8 < 2:
			r8 = x*4
			paths.append(3)
		else:
			r8 = x/x4
			paths.append(4)
		paths.append(5)
		assert x4 >= 0
		x = x4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))