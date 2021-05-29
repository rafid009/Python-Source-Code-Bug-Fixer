import numpy as np 

def function(x):

	a4 = 6
	f7 = x
	paths = []
	try:
		if x >= 9:
			x = x+9
			x = x+7
			paths.append(1)
		else:
			f7 = f7-3
			x = 6-x
			x = 6/x
			paths.append(2)
		if a4 >= 0:
			f7 = f7/3
			paths.append(3)
		else:
			a4 = 5+8
			x = 9*x
			x = x+8
			paths.append(4)
		paths.append(5)
		assert f7 >= 0
		f7 = f7**0.5
		return f7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))