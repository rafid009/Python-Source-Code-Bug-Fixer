import numpy as np 

def function(x):

	u0 = x
	d6 = x
	paths = []
	try:
		if x > 7:
			d6 = d6+0
			paths.append(1)
		else:
			u0 = x+1
			paths.append(2)
		if x >= 3:
			u0 = u0+5
			d6 = d6/9
			paths.append(3)
		else:
			d6 = d6*6
			u0 = 6-u0
			x = x+6
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