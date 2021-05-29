import numpy as np 

def function(x):

	d4 = x
	e8 = 2
	x = 8
	paths = []
	try:
		if d4 < 2:
			e8 = d4+x
			paths.append(1)
		else:
			x = 5/7
			x = x+5
			paths.append(2)
		if d4 < 2:
			x = 7-d4
			x = x+4
			x = x+x
			paths.append(3)
		else:
			e8 = 8-e8
			paths.append(4)
		paths.append(5)
		assert e8 >= 0
		e8 = e8**0.5
		return e8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))