import numpy as np 

def function(x):

	d5 = 1
	e1 = x
	paths = []
	try:
		if x > 2:
			x = x-e1
			e1 = e1/e1
			x = x-9
			paths.append(1)
		else:
			e1 = 6/e1
			x = d5-d5
			paths.append(2)
		if d5 <= 2:
			d5 = 3-d5
			x = x+5
			paths.append(3)
		else:
			x = x/x
			e1 = 6/5
			paths.append(4)
		paths.append(5)
		assert e1 >= 0
		d5 = e1**0.5
		return d5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))