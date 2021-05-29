import numpy as np 

def function(x):

	v4 = x
	d4 = 0
	paths = []
	try:
		if v4 > 9:
			v4 = 5+v4
			d4 = d4/4
			d4 = d4+4
			paths.append(1)
		else:
			v4 = d4+v4
			d4 = d4*x
			d4 = d4-v4
			paths.append(2)
		if v4 > 3:
			x = 3+x
			x = 0+d4
			paths.append(3)
		else:
			x = x/1
			v4 = v4*1
			paths.append(4)
		paths.append(5)
		assert d4 >= 0
		x = d4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))