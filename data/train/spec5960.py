import numpy as np 

def function(x):

	n6 = 2
	d6 = x
	x = 6
	paths = []
	try:
		if d6 <= 1:
			x = 3*4
			d6 = n6/d6
			x = 0/9
			paths.append(1)
		else:
			n6 = d6*n6
			x = 9-x
			paths.append(2)
		if x > 5:
			x = x-x
			d6 = 6/n6
			d6 = 5*d6
			paths.append(3)
		else:
			d6 = 7*8
			d6 = x-8
			n6 = n6*7
			paths.append(4)
		paths.append(5)
		assert d6 >= 0
		n6 = d6**0.5
		return n6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))