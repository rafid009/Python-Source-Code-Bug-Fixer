import numpy as np 

def function(x):

	n9 = 4
	d2 = x
	paths = []
	try:
		if x <= 4:
			d2 = d2+6
			paths.append(1)
		else:
			d2 = n9*d2
			x = 8/9
			paths.append(2)
		if x > 5:
			d2 = d2*5
			n9 = 9-n9
			paths.append(3)
		else:
			d2 = d2/5
			x = x+5
			paths.append(4)
		paths.append(5)
		assert d2 >= 0
		x = d2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))