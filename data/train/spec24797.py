import numpy as np 

def function(x):

	w4 = 8
	d6 = 6
	paths = []
	try:
		if d6 <= 4:
			w4 = w4+w4
			x = 8*x
			paths.append(1)
		else:
			x = x+7
			x = 9-x
			paths.append(2)
		if x <= 6:
			x = x+1
			d6 = 1/d6
			x = 9*8
			paths.append(3)
		else:
			d6 = d6-w4
			paths.append(4)
		paths.append(5)
		assert d6 >= 0
		d6 = d6**0.5
		return d6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))