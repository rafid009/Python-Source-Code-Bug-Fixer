import numpy as np 

def function(x):

	y3 = x
	r4 = x
	paths = []
	try:
		if r4 > 2:
			r4 = 9*r4
			r4 = r4/x
			paths.append(1)
		else:
			r4 = r4+r4
			x = r4/y3
			y3 = 9+y3
			paths.append(2)
		if y3 <= 2:
			r4 = 8-r4
			r4 = r4+x
			paths.append(3)
		else:
			y3 = r4/y3
			paths.append(4)
		paths.append(5)
		assert y3 >= 0
		r4 = y3**0.5
		return r4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))