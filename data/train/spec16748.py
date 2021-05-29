import numpy as np 

def function(x):

	d4 = 3
	y5 = 5
	paths = []
	try:
		if y5 >= 1:
			x = x-d4
			d4 = x-3
			paths.append(1)
		else:
			d4 = x*d4
			d4 = d4*0
			paths.append(2)
		if y5 > 5:
			d4 = 7+d4
			d4 = d4-6
			paths.append(3)
		else:
			x = x/1
			d4 = 3*d4
			paths.append(4)
		paths.append(5)
		assert d4 >= 0
		y5 = d4**0.5
		return y5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))