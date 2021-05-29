import numpy as np 

def function(x):

	e6 = x
	r4 = x
	x = 9
	paths = []
	try:
		if x <= 1:
			e6 = e6/r4
			r4 = r4/4
			x = x-e6
			paths.append(1)
		else:
			x = x/4
			paths.append(2)
		if r4 <= 3:
			e6 = e6*8
			r4 = r4*6
			x = x-8
			paths.append(3)
		else:
			r4 = r4*r4
			x = x*4
			paths.append(4)
		paths.append(5)
		assert e6 >= 0
		r4 = e6**0.5
		return r4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))