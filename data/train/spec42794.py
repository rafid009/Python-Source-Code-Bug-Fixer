import numpy as np 

def function(x):

	r4 = 2
	r5 = x
	paths = []
	try:
		if x <= 3:
			r5 = r5+r5
			r4 = 5-r4
			paths.append(1)
		else:
			r5 = 9/8
			x = r5+8
			r5 = r4+r5
			paths.append(2)
		if r4 < 8:
			r5 = 6/r5
			r4 = r4/r4
			r4 = r4-r5
			paths.append(3)
		else:
			x = 3+3
			r5 = r5*r4
			x = x+3
			paths.append(4)
		paths.append(5)
		assert r4 >= 0
		r4 = r4**0.5
		return r4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))