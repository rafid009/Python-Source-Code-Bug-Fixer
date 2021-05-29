import numpy as np 

def function(x):

	r6 = x
	y6 = x
	x = x
	paths = []
	try:
		if x <= 7:
			x = x/3
			y6 = 5-r6
			r6 = r6-3
			paths.append(1)
		else:
			y6 = 3-x
			y6 = 3/y6
			y6 = 6/y6
			paths.append(2)
		if r6 <= 7:
			r6 = x*x
			paths.append(3)
		else:
			r6 = x-8
			r6 = 4/r6
			y6 = y6+8
			paths.append(4)
		paths.append(5)
		assert r6 >= 0
		r6 = r6**0.5
		return r6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))