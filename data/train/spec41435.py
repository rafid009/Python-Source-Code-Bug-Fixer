import numpy as np 

def function(x):

	y5 = x
	r9 = x
	x = 9
	paths = []
	try:
		if y5 >= 4:
			r9 = 8/r9
			y5 = r9/y5
			x = 8-x
			paths.append(1)
		else:
			x = x*8
			paths.append(2)
		if r9 >= 0:
			r9 = r9*0
			x = x-4
			paths.append(3)
		else:
			x = x*x
			x = 2-7
			y5 = y5*x
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