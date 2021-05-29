import numpy as np 

def function(x):

	f4 = 4
	x7 = x
	paths = []
	try:
		if x >= 2:
			x7 = x7*x
			paths.append(1)
		else:
			f4 = x/4
			x = x*6
			x7 = x7+x7
			paths.append(2)
		if x >= 8:
			f4 = x*4
			paths.append(3)
		else:
			x = 3+x7
			x = x+2
			f4 = f4-0
			paths.append(4)
		paths.append(5)
		assert f4 >= 0
		x7 = f4**0.5
		return x7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))