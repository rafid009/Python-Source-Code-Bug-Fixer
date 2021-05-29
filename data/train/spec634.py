import numpy as np 

def function(x):

	y4 = x
	d6 = 6
	paths = []
	try:
		if d6 < 2:
			d6 = d6-y4
			d6 = y4-d6
			y4 = y4*4
			paths.append(1)
		else:
			d6 = 2-d6
			paths.append(2)
		if d6 <= 0:
			x = x+y4
			paths.append(3)
		else:
			y4 = d6+x
			x = 1*d6
			paths.append(4)
		paths.append(5)
		assert y4 >= 0
		d6 = y4**0.5
		return d6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))