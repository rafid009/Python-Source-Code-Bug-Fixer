import numpy as np 

def function(x):

	x4 = 5
	r0 = x
	paths = []
	try:
		if x4 > 6:
			x = r0-x
			x4 = 2/x4
			x4 = r0*0
			paths.append(1)
		else:
			x = x+9
			x4 = r0*6
			x4 = x4+x
			paths.append(2)
		if r0 > 2:
			x4 = x4-0
			x4 = 4+x4
			paths.append(3)
		else:
			r0 = 3+r0
			r0 = r0+3
			x4 = 8*x4
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