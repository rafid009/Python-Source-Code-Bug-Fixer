import numpy as np 

def function(x):

	a5 = x
	a6 = x
	paths = []
	try:
		if a6 > 3:
			a6 = 1*7
			x = 1+x
			a5 = a5-a6
			paths.append(1)
		else:
			a6 = a6-9
			paths.append(2)
		if a6 > 7:
			x = 8+x
			a5 = a5/9
			paths.append(3)
		else:
			a5 = 6-x
			paths.append(4)
		paths.append(5)
		assert a5 >= 0
		x = a5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))