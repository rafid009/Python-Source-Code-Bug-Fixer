import numpy as np 

def function(x):

	v4 = x
	u0 = x
	x = x
	paths = []
	try:
		if x > 8:
			v4 = 1-0
			v4 = v4*9
			paths.append(1)
		else:
			u0 = v4+u0
			v4 = u0*5
			paths.append(2)
		if x >= 9:
			v4 = v4/v4
			paths.append(3)
		else:
			v4 = u0+v4
			x = 5+0
			paths.append(4)
		paths.append(5)
		assert v4 >= 0
		v4 = v4**0.5
		return v4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))