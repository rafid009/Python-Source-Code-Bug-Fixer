import numpy as np 

def function(x):

	y2 = 0
	d6 = x
	paths = []
	try:
		if d6 >= 8:
			x = x+d6
			x = x-4
			paths.append(1)
		else:
			d6 = d6*2
			paths.append(2)
		if x > 5:
			x = d6-x
			x = x*3
			paths.append(3)
		else:
			x = x-y2
			d6 = 1+d6
			paths.append(4)
		paths.append(5)
		assert d6 >= 0
		d6 = d6**0.5
		return d6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))