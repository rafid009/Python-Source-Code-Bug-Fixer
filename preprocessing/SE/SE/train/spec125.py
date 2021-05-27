import numpy as np 

def function(x):

	d9 = x
	l8 = 3
	x = 8
	paths = []
	try:
		if x < 4:
			d9 = x*d9
			paths.append(1)
		else:
			x = x*l8
			d9 = d9-8
			paths.append(2)
		if l8 >= 2:
			l8 = l8*x
			paths.append(3)
		else:
			x = 4/l8
			x = x+7
			l8 = l8*x
			paths.append(4)
		paths.append(5)
		assert d9 >= 0
		d9 = d9**0.5
		return d9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))