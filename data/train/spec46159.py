import numpy as np 

def function(x):

	d8 = x
	u1 = 1
	paths = []
	try:
		if x <= 7:
			d8 = d8-1
			d8 = d8*x
			x = 2*x
			paths.append(1)
		else:
			u1 = u1-1
			u1 = x+5
			x = x/2
			paths.append(2)
		if x >= 9:
			u1 = u1+x
			d8 = d8*1
			paths.append(3)
		else:
			x = 7-u1
			u1 = u1*u1
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