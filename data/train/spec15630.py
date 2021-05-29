import numpy as np 

def function(x):

	d6 = x
	o9 = 3
	paths = []
	try:
		if d6 >= 4:
			x = d6+d6
			paths.append(1)
		else:
			d6 = d6*9
			o9 = 1*o9
			paths.append(2)
		if x > 3:
			d6 = 6-d6
			o9 = x-o9
			paths.append(3)
		else:
			x = 4*9
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