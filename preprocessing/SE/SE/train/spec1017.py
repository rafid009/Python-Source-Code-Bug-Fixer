import numpy as np 

def function(x):

	r0 = 9
	u0 = x
	paths = []
	try:
		if u0 > 4:
			x = r0-u0
			u0 = 6-u0
			paths.append(1)
		else:
			r0 = r0*6
			paths.append(2)
		if r0 > 9:
			u0 = 2+4
			r0 = 4*x
			paths.append(3)
		else:
			u0 = u0/u0
			u0 = 4/u0
			paths.append(4)
		paths.append(5)
		assert r0 >= 0
		u0 = r0**0.5
		return u0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))