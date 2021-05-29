import numpy as np 

def function(x):

	r2 = 6
	e0 = 6
	paths = []
	try:
		if x >= 4:
			r2 = x-e0
			paths.append(1)
		else:
			r2 = r2*7
			e0 = e0+5
			x = 7-x
			paths.append(2)
		if e0 < 0:
			x = 7*0
			paths.append(3)
		else:
			e0 = e0+7
			x = 1/x
			x = x-8
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