import numpy as np 

def function(x):

	o7 = 7
	e2 = x
	x = 8
	paths = []
	try:
		if x <= 6:
			e2 = 5/o7
			paths.append(1)
		else:
			e2 = 5/e2
			x = 3+e2
			paths.append(2)
		if x > 0:
			e2 = 7/7
			o7 = o7+8
			o7 = 0/o7
			paths.append(3)
		else:
			x = 4/8
			x = 0+x
			paths.append(4)
		paths.append(5)
		assert e2 >= 0
		x = e2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))