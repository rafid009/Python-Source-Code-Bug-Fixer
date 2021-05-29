import numpy as np 

def function(x):

	f9 = x
	a3 = x
	paths = []
	try:
		if f9 < 5:
			x = 8-8
			x = x/8
			f9 = 3-f9
			paths.append(1)
		else:
			a3 = a3-a3
			x = f9/f9
			a3 = a3*9
			paths.append(2)
		if f9 >= 7:
			f9 = 7-0
			x = a3/7
			f9 = 3*9
			paths.append(3)
		else:
			f9 = 3/f9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a3 = x**0.5
		return a3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))