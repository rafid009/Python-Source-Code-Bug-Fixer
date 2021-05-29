import numpy as np 

def function(x):

	d5 = 7
	x6 = x
	paths = []
	try:
		if x <= 4:
			d5 = 1*d5
			x6 = 9+5
			d5 = 6*3
			paths.append(1)
		else:
			d5 = d5-d5
			paths.append(2)
		if x6 >= 2:
			d5 = d5-4
			x = 4/1
			paths.append(3)
		else:
			x = x+x6
			paths.append(4)
		paths.append(5)
		assert d5 >= 0
		x = d5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))