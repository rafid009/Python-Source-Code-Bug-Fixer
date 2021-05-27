import numpy as np 

def function(x):

	a7 = x
	e8 = 3
	x = x
	paths = []
	try:
		if x <= 6:
			e8 = 5*x
			a7 = a7+x
			a7 = a7*2
			paths.append(1)
		else:
			x = e8/2
			paths.append(2)
		if x < 6:
			e8 = 9+e8
			x = a7-3
			paths.append(3)
		else:
			a7 = e8*1
			paths.append(4)
		paths.append(5)
		assert e8 >= 0
		x = e8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))