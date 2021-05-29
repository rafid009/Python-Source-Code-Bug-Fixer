import numpy as np 

def function(x):

	x8 = x
	r2 = 5
	paths = []
	try:
		if x <= 4:
			x8 = 8+x8
			r2 = r2+r2
			r2 = r2*1
			paths.append(1)
		else:
			r2 = 4*5
			x = 9+x
			paths.append(2)
		if r2 < 2:
			x8 = 4/5
			r2 = r2+x8
			x8 = x8-x8
			paths.append(3)
		else:
			x8 = x8*x
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