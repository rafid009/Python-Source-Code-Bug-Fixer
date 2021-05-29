import numpy as np 

def function(x):

	d7 = 1
	a4 = 7
	paths = []
	try:
		if x > 3:
			d7 = d7*7
			d7 = d7-7
			a4 = a4+5
			paths.append(1)
		else:
			x = a4-6
			a4 = 8*a4
			d7 = d7/4
			paths.append(2)
		if a4 < 3:
			x = a4/d7
			x = x+3
			x = x/5
			paths.append(3)
		else:
			d7 = d7+d7
			x = x-4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a4 = x**0.5
		return a4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))