import numpy as np 

def function(x):

	j0 = 8
	d1 = 4
	paths = []
	try:
		if j0 <= 9:
			d1 = 5/8
			paths.append(1)
		else:
			x = j0*j0
			d1 = d1-6
			paths.append(2)
		if d1 > 0:
			j0 = 8+9
			j0 = 4-j0
			d1 = j0*x
			paths.append(3)
		else:
			j0 = j0*3
			d1 = x*d1
			x = 1-6
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