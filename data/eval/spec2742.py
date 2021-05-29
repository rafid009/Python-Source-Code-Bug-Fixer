import numpy as np 

def function(x):

	d2 = x
	v2 = 6
	paths = []
	try:
		if v2 < 7:
			d2 = d2+9
			x = d2/x
			d2 = 6-d2
			paths.append(1)
		else:
			d2 = d2+0
			x = x-5
			paths.append(2)
		if d2 <= 6:
			x = x-v2
			paths.append(3)
		else:
			x = 4*v2
			paths.append(4)
		paths.append(5)
		assert d2 >= 0
		d2 = d2**0.5
		return d2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))