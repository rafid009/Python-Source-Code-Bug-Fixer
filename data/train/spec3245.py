import numpy as np 

def function(x):

	f8 = x
	a8 = 5
	paths = []
	try:
		if a8 >= 1:
			x = x*4
			a8 = a8+a8
			x = x-0
			paths.append(1)
		else:
			x = 1-x
			x = x*x
			paths.append(2)
		if a8 <= 8:
			a8 = f8+a8
			paths.append(3)
		else:
			a8 = 4-a8
			x = x/1
			x = 5*x
			paths.append(4)
		paths.append(5)
		assert f8 >= 0
		a8 = f8**0.5
		return a8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))