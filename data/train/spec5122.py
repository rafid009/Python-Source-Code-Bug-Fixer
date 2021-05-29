import numpy as np 

def function(x):

	d2 = 9
	a7 = x
	paths = []
	try:
		if a7 >= 3:
			d2 = d2+x
			paths.append(1)
		else:
			x = x-3
			a7 = 4*a7
			paths.append(2)
		if a7 > 8:
			d2 = a7*5
			paths.append(3)
		else:
			d2 = x*a7
			x = x-7
			a7 = 5/a7
			paths.append(4)
		paths.append(5)
		assert a7 >= 0
		d2 = a7**0.5
		return d2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))