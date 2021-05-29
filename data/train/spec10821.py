import numpy as np 

def function(x):

	r0 = 2
	y4 = 7
	paths = []
	try:
		if y4 >= 6:
			r0 = r0/4
			paths.append(1)
		else:
			x = r0*x
			paths.append(2)
		if r0 > 4:
			y4 = y4/x
			paths.append(3)
		else:
			r0 = r0+0
			y4 = y4+x
			paths.append(4)
		paths.append(5)
		assert y4 >= 0
		r0 = y4**0.5
		return r0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))