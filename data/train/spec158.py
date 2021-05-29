import numpy as np 

def function(x):

	e1 = x
	d7 = 8
	paths = []
	try:
		if e1 < 1:
			x = 4+3
			paths.append(1)
		else:
			x = d7+x
			d7 = 6*d7
			paths.append(2)
		if e1 > 2:
			x = 2-9
			d7 = 9/1
			paths.append(3)
		else:
			e1 = e1-x
			paths.append(4)
		paths.append(5)
		assert e1 >= 0
		x = e1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))