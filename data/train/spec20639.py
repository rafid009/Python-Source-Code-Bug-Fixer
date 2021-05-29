import numpy as np 

def function(x):

	d8 = x
	a6 = x
	paths = []
	try:
		if d8 >= 5:
			x = x/d8
			d8 = d8+d8
			paths.append(1)
		else:
			a6 = 8-d8
			d8 = 3*6
			d8 = d8/a6
			paths.append(2)
		if a6 <= 7:
			a6 = a6-4
			a6 = x*a6
			paths.append(3)
		else:
			d8 = d8*a6
			d8 = d8/d8
			a6 = a6-8
			paths.append(4)
		paths.append(5)
		assert a6 >= 0
		a6 = a6**0.5
		return a6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))