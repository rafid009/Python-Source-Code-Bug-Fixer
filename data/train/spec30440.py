import numpy as np 

def function(x):

	r4 = 5
	d4 = x
	x = 6
	paths = []
	try:
		if x <= 0:
			d4 = 0/r4
			paths.append(1)
		else:
			d4 = d4+d4
			paths.append(2)
		if r4 >= 5:
			d4 = x+d4
			paths.append(3)
		else:
			r4 = 2/5
			r4 = r4-2
			d4 = d4-2
			paths.append(4)
		paths.append(5)
		assert d4 >= 0
		r4 = d4**0.5
		return r4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))