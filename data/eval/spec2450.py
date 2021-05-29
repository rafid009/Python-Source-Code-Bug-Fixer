import numpy as np 

def function(x):

	o9 = x
	a7 = 5
	paths = []
	try:
		if o9 < 7:
			a7 = a7*9
			a7 = 7/a7
			o9 = 4+x
			paths.append(1)
		else:
			x = 3/1
			paths.append(2)
		if o9 >= 9:
			x = 4/x
			paths.append(3)
		else:
			x = x-7
			x = x+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a7 = x**0.5
		return a7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))