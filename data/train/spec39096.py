import numpy as np 

def function(x):

	d7 = x
	a1 = 6
	paths = []
	try:
		if a1 > 8:
			d7 = d7/5
			x = 2/x
			paths.append(1)
		else:
			a1 = x/a1
			x = x*6
			paths.append(2)
		if d7 <= 6:
			d7 = 3-6
			paths.append(3)
		else:
			a1 = 1*a1
			paths.append(4)
		paths.append(5)
		assert a1 >= 0
		x = a1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))