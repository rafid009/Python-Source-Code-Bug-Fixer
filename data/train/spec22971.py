import numpy as np 

def function(x):

	d9 = x
	e1 = 4
	paths = []
	try:
		if e1 < 4:
			d9 = 8/d9
			d9 = d9*3
			d9 = 1+d9
			paths.append(1)
		else:
			x = 1*e1
			x = 4-6
			d9 = d9+x
			paths.append(2)
		if x < 0:
			e1 = d9-x
			d9 = e1/4
			paths.append(3)
		else:
			x = e1-e1
			x = 6+x
			x = x-d9
			paths.append(4)
		paths.append(5)
		assert d9 >= 0
		e1 = d9**0.5
		return e1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))