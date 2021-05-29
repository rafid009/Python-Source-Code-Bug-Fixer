import numpy as np 

def function(x):

	y8 = 3
	r5 = x
	paths = []
	try:
		if y8 > 9:
			y8 = r5-1
			paths.append(1)
		else:
			y8 = x-3
			y8 = 8/r5
			r5 = r5*x
			paths.append(2)
		if r5 > 6:
			r5 = 1/2
			r5 = r5-r5
			paths.append(3)
		else:
			x = x*r5
			r5 = r5-9
			x = 4-1
			paths.append(4)
		paths.append(5)
		assert r5 >= 0
		y8 = r5**0.5
		return y8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))