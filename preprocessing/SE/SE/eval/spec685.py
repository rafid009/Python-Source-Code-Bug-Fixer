import numpy as np 

def function(x):

	a4 = 4
	d1 = x
	x = 3
	paths = []
	try:
		if d1 >= 3:
			d1 = d1/4
			paths.append(1)
		else:
			x = 5-1
			a4 = d1*x
			x = 6+5
			paths.append(2)
		if d1 >= 4:
			a4 = a4-9
			a4 = 2/a4
			paths.append(3)
		else:
			d1 = d1-2
			d1 = d1+0
			paths.append(4)
		paths.append(5)
		assert a4 >= 0
		x = a4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))