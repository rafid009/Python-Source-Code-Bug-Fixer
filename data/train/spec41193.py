import numpy as np 

def function(x):

	e7 = 6
	u5 = 4
	paths = []
	try:
		if e7 < 6:
			x = e7+4
			paths.append(1)
		else:
			e7 = 1*x
			x = 3/5
			paths.append(2)
		if x > 4:
			e7 = e7+x
			paths.append(3)
		else:
			x = x+3
			e7 = e7+0
			paths.append(4)
		paths.append(5)
		assert e7 >= 0
		x = e7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))