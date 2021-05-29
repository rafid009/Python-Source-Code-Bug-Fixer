import numpy as np 

def function(x):

	d5 = x
	k2 = x
	paths = []
	try:
		if d5 <= 1:
			x = 5*x
			x = 4-k2
			paths.append(1)
		else:
			k2 = k2-k2
			paths.append(2)
		if k2 > 0:
			k2 = k2+2
			paths.append(3)
		else:
			d5 = d5/6
			x = x+5
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