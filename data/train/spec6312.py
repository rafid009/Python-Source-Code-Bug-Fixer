import numpy as np 

def function(x):

	r2 = x
	paths = []
	try:
		if x >= 4:
			x = r2-x
			x = r2-x
			x = x-1
			paths.append(1)
		else:
			r2 = r2-4
			r2 = r2/2
			x = 0+6
			paths.append(2)
		if r2 < 2:
			r2 = 6+r2
			r2 = r2+3
			paths.append(3)
		else:
			r2 = x-r2
			x = 1-x
			paths.append(4)
		paths.append(5)
		assert r2 >= 0
		x = r2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))