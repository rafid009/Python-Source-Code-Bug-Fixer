import numpy as np 

def function(x):

	v6 = x
	d5 = x
	paths = []
	try:
		if d5 > 7:
			d5 = 8-d5
			d5 = v6-3
			paths.append(1)
		else:
			d5 = x-v6
			paths.append(2)
		if v6 > 5:
			d5 = d5*9
			x = x+v6
			d5 = 5-x
			paths.append(3)
		else:
			x = x-9
			v6 = 6*4
			v6 = v6-6
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