import numpy as np 

def function(x):

	d8 = x
	e5 = x
	paths = []
	try:
		if d8 > 4:
			e5 = e5+x
			e5 = x+d8
			paths.append(1)
		else:
			e5 = e5*7
			x = x+9
			paths.append(2)
		if x > 6:
			e5 = e5-2
			e5 = e5+7
			paths.append(3)
		else:
			x = x+d8
			e5 = e5*4
			x = x+d8
			paths.append(4)
		paths.append(5)
		assert d8 >= 0
		x = d8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))