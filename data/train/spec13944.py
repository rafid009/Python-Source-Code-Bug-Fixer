import numpy as np 

def function(x):

	d6 = x
	d1 = x
	x = 4
	paths = []
	try:
		if d6 >= 1:
			x = 9-7
			d1 = 0/1
			paths.append(1)
		else:
			d6 = 9*9
			paths.append(2)
		if x < 4:
			d1 = 6+2
			paths.append(3)
		else:
			d1 = 6/d1
			paths.append(4)
		paths.append(5)
		assert d1 >= 0
		d6 = d1**0.5
		return d6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))