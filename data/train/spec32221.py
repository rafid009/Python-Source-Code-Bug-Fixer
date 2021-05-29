import numpy as np 

def function(x):

	e4 = x
	a1 = x
	paths = []
	try:
		if e4 > 5:
			a1 = 7+9
			paths.append(1)
		else:
			a1 = a1*8
			paths.append(2)
		if e4 < 2:
			a1 = a1*3
			a1 = 3-x
			a1 = 7/e4
			paths.append(3)
		else:
			a1 = 5-7
			a1 = a1+3
			paths.append(4)
		paths.append(5)
		assert e4 >= 0
		a1 = e4**0.5
		return a1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))