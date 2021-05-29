import numpy as np 

def function(x):

	r0 = x
	u3 = 5
	paths = []
	try:
		if x >= 3:
			r0 = u3*x
			x = x/7
			u3 = 2/u3
			paths.append(1)
		else:
			r0 = r0*4
			x = r0/x
			paths.append(2)
		if r0 < 6:
			x = 0*9
			paths.append(3)
		else:
			r0 = 1+6
			paths.append(4)
		paths.append(5)
		assert r0 >= 0
		x = r0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))