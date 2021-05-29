import numpy as np 

def function(x):

	d1 = x
	q8 = x
	paths = []
	try:
		if q8 <= 3:
			q8 = q8+0
			x = x+q8
			paths.append(1)
		else:
			q8 = 7/d1
			paths.append(2)
		if q8 < 6:
			x = d1+x
			paths.append(3)
		else:
			x = 0*x
			d1 = d1+d1
			x = 8-x
			paths.append(4)
		paths.append(5)
		assert d1 >= 0
		d1 = d1**0.5
		return d1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))