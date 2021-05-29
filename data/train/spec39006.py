import numpy as np 

def function(x):

	n7 = x
	d7 = 6
	paths = []
	try:
		if d7 <= 4:
			x = d7/n7
			n7 = d7+n7
			paths.append(1)
		else:
			n7 = 8/x
			paths.append(2)
		if d7 < 8:
			d7 = d7*2
			d7 = n7-d7
			x = x/6
			paths.append(3)
		else:
			n7 = d7+0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d7 = x**0.5
		return d7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))