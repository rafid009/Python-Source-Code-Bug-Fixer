import numpy as np 

def function(x):

	d6 = 0
	n8 = 6
	paths = []
	try:
		if d6 >= 8:
			d6 = d6/8
			d6 = d6-6
			x = x-9
			paths.append(1)
		else:
			n8 = d6*n8
			n8 = x/5
			x = 4*4
			paths.append(2)
		if d6 >= 6:
			d6 = x+d6
			d6 = 6/5
			n8 = 4*n8
			paths.append(3)
		else:
			x = n8*x
			d6 = 2/9
			x = x*1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d6 = x**0.5
		return d6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))