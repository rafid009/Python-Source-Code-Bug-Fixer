import numpy as np 

def function(x):

	v4 = 3
	r5 = 3
	paths = []
	try:
		if x <= 9:
			v4 = v4/4
			x = x*2
			paths.append(1)
		else:
			x = 6*1
			v4 = v4*2
			paths.append(2)
		if x < 6:
			r5 = r5/3
			paths.append(3)
		else:
			r5 = r5+4
			v4 = v4-0
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