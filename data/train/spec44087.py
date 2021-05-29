import numpy as np 

def function(x):

	y5 = x
	r0 = 8
	paths = []
	try:
		if y5 > 6:
			y5 = y5*x
			r0 = 7-5
			paths.append(1)
		else:
			r0 = x-r0
			r0 = 3+r0
			paths.append(2)
		if x >= 5:
			r0 = 7-1
			r0 = r0*2
			y5 = y5+1
			paths.append(3)
		else:
			y5 = y5/3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y5 = x**0.5
		return y5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))