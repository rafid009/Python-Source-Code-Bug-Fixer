import numpy as np 

def function(x):

	b6 = x
	d8 = x
	paths = []
	try:
		if x >= 5:
			x = 1-x
			b6 = 9+b6
			b6 = x-b6
			paths.append(1)
		else:
			d8 = d8+7
			x = 6/x
			d8 = 5*d8
			paths.append(2)
		if b6 >= 1:
			d8 = 3-d8
			paths.append(3)
		else:
			b6 = 5+b6
			x = 4/x
			b6 = 6+0
			paths.append(4)
		paths.append(5)
		assert d8 >= 0
		b6 = d8**0.5
		return b6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))