import numpy as np 

def function(x):

	v0 = x
	u6 = 5
	paths = []
	try:
		if u6 < 7:
			u6 = u6*u6
			paths.append(1)
		else:
			x = 3/x
			u6 = u6-4
			u6 = u6-3
			paths.append(2)
		if v0 < 3:
			v0 = v0+9
			v0 = 5*v0
			x = x-5
			paths.append(3)
		else:
			v0 = 1+v0
			x = x+3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v0 = x**0.5
		return v0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))