import numpy as np 

def function(x):

	j6 = 5
	d5 = 2
	paths = []
	try:
		if x < 8:
			j6 = j6+0
			d5 = x-d5
			d5 = d5-x
			paths.append(1)
		else:
			x = 9*x
			paths.append(2)
		if x <= 7:
			d5 = 6/d5
			j6 = j6*j6
			paths.append(3)
		else:
			x = x/j6
			d5 = d5+4
			d5 = 7*d5
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