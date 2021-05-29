import numpy as np 

def function(x):

	r0 = 3
	u9 = 0
	paths = []
	try:
		if r0 >= 1:
			r0 = x/r0
			paths.append(1)
		else:
			x = 4/r0
			paths.append(2)
		if x < 6:
			x = x+1
			x = r0+6
			paths.append(3)
		else:
			x = r0*x
			paths.append(4)
		paths.append(5)
		assert r0 >= 0
		r0 = r0**0.5
		return r0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))