import numpy as np 

def function(x):

	d6 = x
	a3 = 9
	x = x
	paths = []
	try:
		if a3 >= 0:
			x = 4+d6
			d6 = 8*d6
			d6 = 9-a3
			paths.append(1)
		else:
			x = 5*2
			paths.append(2)
		if x >= 8:
			a3 = a3/4
			d6 = 4*d6
			paths.append(3)
		else:
			x = 9-x
			a3 = x-5
			d6 = 2+6
			paths.append(4)
		paths.append(5)
		assert a3 >= 0
		a3 = a3**0.5
		return a3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))