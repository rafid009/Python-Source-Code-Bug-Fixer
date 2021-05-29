import numpy as np 

def function(x):

	u1 = x
	r5 = 6
	paths = []
	try:
		if x <= 8:
			u1 = x*6
			r5 = 2+4
			paths.append(1)
		else:
			x = 8-x
			paths.append(2)
		if u1 > 6:
			r5 = 1+2
			paths.append(3)
		else:
			u1 = 2+r5
			u1 = 4-u1
			x = r5+0
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