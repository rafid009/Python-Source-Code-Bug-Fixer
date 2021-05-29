import numpy as np 

def function(x):

	n9 = 0
	d1 = x
	paths = []
	try:
		if d1 > 4:
			n9 = n9-1
			n9 = n9+5
			d1 = d1+n9
			paths.append(1)
		else:
			n9 = d1*0
			paths.append(2)
		if d1 < 3:
			n9 = 4-n9
			paths.append(3)
		else:
			n9 = 2+n9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d1 = x**0.5
		return d1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))