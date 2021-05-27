import numpy as np 

def function(x):

	d8 = x
	w6 = x
	paths = []
	try:
		if x < 9:
			x = x-4
			d8 = d8-x
			d8 = w6/9
			paths.append(1)
		else:
			x = x-d8
			w6 = x+6
			paths.append(2)
		if d8 > 4:
			d8 = 1-d8
			d8 = d8+3
			x = x*9
			paths.append(3)
		else:
			x = x-w6
			paths.append(4)
		paths.append(5)
		assert w6 >= 0
		d8 = w6**0.5
		return d8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))