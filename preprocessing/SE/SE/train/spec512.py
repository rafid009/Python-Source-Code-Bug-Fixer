import numpy as np 

def function(x):

	r9 = 3
	d2 = x
	paths = []
	try:
		if d2 < 9:
			d2 = d2*d2
			r9 = r9-d2
			paths.append(1)
		else:
			x = 6*x
			d2 = d2*3
			paths.append(2)
		if x > 9:
			d2 = 6+6
			paths.append(3)
		else:
			x = 3*x
			x = x/3
			d2 = x/x
			paths.append(4)
		paths.append(5)
		assert r9 >= 0
		d2 = r9**0.5
		return d2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))