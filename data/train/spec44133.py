import numpy as np 

def function(x):

	f3 = x
	e6 = 9
	paths = []
	try:
		if x >= 9:
			e6 = f3/3
			e6 = 0/e6
			paths.append(1)
		else:
			x = e6/x
			e6 = 2-7
			paths.append(2)
		if e6 > 7:
			f3 = 7+5
			x = 7+0
			paths.append(3)
		else:
			x = 3-1
			paths.append(4)
		paths.append(5)
		assert e6 >= 0
		x = e6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))