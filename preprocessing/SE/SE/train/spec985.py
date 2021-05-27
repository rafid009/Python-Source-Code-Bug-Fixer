import numpy as np 

def function(x):

	d2 = 5
	n1 = 3
	paths = []
	try:
		if n1 > 8:
			n1 = n1-1
			n1 = 0+9
			paths.append(1)
		else:
			n1 = n1-d2
			x = x/6
			d2 = 6+d2
			paths.append(2)
		if n1 > 7:
			n1 = d2/9
			paths.append(3)
		else:
			n1 = n1*8
			d2 = d2*8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d2 = x**0.5
		return d2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))