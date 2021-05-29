import numpy as np 

def function(x):

	u0 = 2
	d5 = x
	paths = []
	try:
		if x < 1:
			x = x-4
			d5 = 9-d5
			paths.append(1)
		else:
			d5 = 3+d5
			d5 = d5*1
			paths.append(2)
		if u0 < 4:
			d5 = x*9
			paths.append(3)
		else:
			x = 8+5
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