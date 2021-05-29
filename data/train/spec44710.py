import numpy as np 

def function(x):

	d5 = x
	v1 = x
	paths = []
	try:
		if v1 >= 0:
			v1 = v1-1
			paths.append(1)
		else:
			d5 = d5*1
			v1 = v1/7
			paths.append(2)
		if v1 <= 2:
			x = 0*8
			v1 = 5*8
			paths.append(3)
		else:
			x = 9-d5
			x = v1-5
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