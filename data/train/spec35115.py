import numpy as np 

def function(x):

	r4 = x
	r5 = x
	paths = []
	try:
		if r5 > 4:
			x = 7/x
			paths.append(1)
		else:
			r4 = r4*9
			r4 = r4*3
			x = r5*5
			paths.append(2)
		if x >= 7:
			x = r5/3
			r5 = r5+r5
			paths.append(3)
		else:
			r4 = r4/r4
			r4 = r4*r5
			paths.append(4)
		paths.append(5)
		assert r4 >= 0
		x = r4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))