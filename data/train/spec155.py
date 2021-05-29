import numpy as np 

def function(x):

	i3 = 7
	d5 = 6
	paths = []
	try:
		if x >= 4:
			x = 1/2
			x = 6+x
			paths.append(1)
		else:
			d5 = i3+d5
			paths.append(2)
		if x >= 6:
			d5 = 0-d5
			x = x-x
			paths.append(3)
		else:
			d5 = 5+4
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