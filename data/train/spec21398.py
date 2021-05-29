import numpy as np 

def function(x):

	d5 = x
	v3 = x
	paths = []
	try:
		if v3 <= 2:
			v3 = v3+v3
			paths.append(1)
		else:
			x = 0/x
			v3 = d5-d5
			paths.append(2)
		if v3 < 9:
			d5 = d5+4
			v3 = 1*v3
			d5 = x+d5
			paths.append(3)
		else:
			d5 = d5/3
			d5 = x-x
			d5 = d5-3
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