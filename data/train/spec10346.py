import numpy as np 

def function(x):

	n8 = x
	d6 = 5
	paths = []
	try:
		if d6 < 2:
			d6 = d6/7
			n8 = n8*5
			paths.append(1)
		else:
			n8 = 9-n8
			n8 = 2/n8
			x = x-8
			paths.append(2)
		if n8 <= 9:
			x = x/x
			n8 = n8*5
			paths.append(3)
		else:
			x = 4/x
			x = x*5
			paths.append(4)
		paths.append(5)
		assert n8 >= 0
		x = n8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))