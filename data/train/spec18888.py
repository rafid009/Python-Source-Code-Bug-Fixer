import numpy as np 

def function(x):

	d8 = x
	k7 = x
	paths = []
	try:
		if d8 < 3:
			k7 = 4*k7
			k7 = k7*4
			paths.append(1)
		else:
			d8 = d8/6
			d8 = 2*1
			paths.append(2)
		if k7 > 6:
			k7 = k7*5
			x = 0*k7
			d8 = 3-2
			paths.append(3)
		else:
			x = 9/d8
			paths.append(4)
		paths.append(5)
		assert d8 >= 0
		d8 = d8**0.5
		return d8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))