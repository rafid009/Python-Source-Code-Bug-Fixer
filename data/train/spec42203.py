import numpy as np 

def function(x):

	n4 = x
	d5 = 9
	paths = []
	try:
		if d5 < 2:
			d5 = 8-9
			n4 = 9/6
			paths.append(1)
		else:
			n4 = n4+d5
			n4 = n4*1
			n4 = d5*x
			paths.append(2)
		if d5 > 4:
			d5 = d5/n4
			paths.append(3)
		else:
			n4 = 5*n4
			d5 = 4/1
			d5 = 8*n4
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