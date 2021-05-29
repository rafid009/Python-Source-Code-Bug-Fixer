import numpy as np 

def function(x):

	n8 = x
	d6 = 7
	paths = []
	try:
		if d6 <= 4:
			d6 = 7*d6
			paths.append(1)
		else:
			d6 = d6+6
			d6 = 1-d6
			paths.append(2)
		if d6 <= 0:
			d6 = d6*0
			x = x*3
			paths.append(3)
		else:
			d6 = 1-7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n8 = x**0.5
		return n8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))