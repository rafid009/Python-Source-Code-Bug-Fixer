import numpy as np 

def function(x):

	y6 = x
	d1 = x
	paths = []
	try:
		if y6 >= 6:
			x = x/1
			paths.append(1)
		else:
			y6 = y6*2
			d1 = d1+5
			paths.append(2)
		if d1 > 5:
			y6 = y6/7
			d1 = d1+8
			d1 = y6/2
			paths.append(3)
		else:
			x = 5/x
			x = x/2
			paths.append(4)
		paths.append(5)
		assert d1 >= 0
		x = d1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))