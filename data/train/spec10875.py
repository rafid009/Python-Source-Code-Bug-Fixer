import numpy as np 

def function(x):

	d8 = 9
	i9 = 6
	paths = []
	try:
		if d8 < 3:
			d8 = 3+d8
			paths.append(1)
		else:
			d8 = d8+x
			x = x/4
			i9 = x+4
			paths.append(2)
		if x <= 1:
			d8 = x/d8
			paths.append(3)
		else:
			x = x/6
			paths.append(4)
		paths.append(5)
		assert d8 >= 0
		d8 = d8**0.5
		return d8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))