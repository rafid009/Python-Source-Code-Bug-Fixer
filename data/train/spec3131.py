import numpy as np 

def function(x):

	e1 = 3
	f4 = x
	paths = []
	try:
		if e1 > 0:
			x = 6*x
			e1 = 4*6
			x = x-x
			paths.append(1)
		else:
			x = x*6
			e1 = e1/7
			x = 4/x
			paths.append(2)
		if x >= 6:
			x = x*8
			e1 = 0-9
			paths.append(3)
		else:
			x = 5*x
			e1 = e1/f4
			paths.append(4)
		paths.append(5)
		assert f4 >= 0
		f4 = f4**0.5
		return f4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))