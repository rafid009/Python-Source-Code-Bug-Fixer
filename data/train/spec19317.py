import numpy as np 

def function(x):

	r4 = x
	u6 = x
	paths = []
	try:
		if u6 > 4:
			u6 = 2+u6
			u6 = 9*8
			r4 = r4+r4
			paths.append(1)
		else:
			r4 = r4/r4
			r4 = r4*4
			paths.append(2)
		if x < 7:
			r4 = 3+r4
			r4 = 1+7
			paths.append(3)
		else:
			u6 = 2*u6
			r4 = 4/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))