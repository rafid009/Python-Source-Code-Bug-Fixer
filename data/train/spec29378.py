import numpy as np 

def function(x):

	d6 = 5
	d5 = x
	paths = []
	try:
		if d5 <= 2:
			d6 = d6-d5
			d6 = 1*d6
			paths.append(1)
		else:
			x = 1+d6
			d5 = x+d5
			d6 = d5-d6
			paths.append(2)
		if x >= 0:
			x = x/d6
			d6 = d6/8
			paths.append(3)
		else:
			d6 = d6*7
			x = x-x
			paths.append(4)
		paths.append(5)
		assert d5 >= 0
		d5 = d5**0.5
		return d5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))