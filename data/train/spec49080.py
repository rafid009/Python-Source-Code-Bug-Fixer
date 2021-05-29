import numpy as np 

def function(x):

	r3 = 2
	d8 = 3
	paths = []
	try:
		if d8 <= 6:
			r3 = d8+5
			paths.append(1)
		else:
			d8 = d8*7
			paths.append(2)
		if r3 <= 9:
			d8 = r3-9
			paths.append(3)
		else:
			r3 = d8+4
			paths.append(4)
		paths.append(5)
		assert d8 >= 0
		x = d8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))