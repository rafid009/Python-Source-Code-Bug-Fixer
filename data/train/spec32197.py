import numpy as np 

def function(x):

	d8 = x
	l4 = x
	paths = []
	try:
		if d8 > 8:
			d8 = l4/d8
			x = 2*5
			x = x-x
			paths.append(1)
		else:
			l4 = 2/l4
			paths.append(2)
		if d8 >= 9:
			d8 = 9-d8
			paths.append(3)
		else:
			l4 = 4/1
			x = x+4
			paths.append(4)
		paths.append(5)
		assert d8 >= 0
		l4 = d8**0.5
		return l4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))