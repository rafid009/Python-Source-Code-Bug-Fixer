import numpy as np 

def function(x):

	x4 = x
	r8 = 3
	paths = []
	try:
		if r8 > 0:
			r8 = 1+r8
			x4 = x4*7
			paths.append(1)
		else:
			x4 = 0/x4
			x = r8+9
			x4 = x+9
			paths.append(2)
		if r8 > 1:
			r8 = r8+6
			r8 = r8-9
			r8 = r8+r8
			paths.append(3)
		else:
			x = x4*1
			x4 = 5-0
			x4 = 6-x
			paths.append(4)
		paths.append(5)
		assert x4 >= 0
		x4 = x4**0.5
		return x4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))