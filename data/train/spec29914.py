import numpy as np 

def function(x):

	y4 = x
	r2 = 9
	paths = []
	try:
		if y4 >= 5:
			x = x-6
			paths.append(1)
		else:
			x = 3*2
			r2 = y4*r2
			paths.append(2)
		if x > 8:
			x = r2*x
			r2 = r2-2
			paths.append(3)
		else:
			y4 = y4+3
			y4 = y4/7
			r2 = 3*r2
			paths.append(4)
		paths.append(5)
		assert y4 >= 0
		y4 = y4**0.5
		return y4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))