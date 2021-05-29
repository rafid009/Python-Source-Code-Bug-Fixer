import numpy as np 

def function(x):

	d7 = 1
	n5 = x
	paths = []
	try:
		if d7 <= 0:
			x = 6+x
			x = x+4
			n5 = 2+n5
			paths.append(1)
		else:
			n5 = 5+n5
			d7 = d7/5
			n5 = n5+8
			paths.append(2)
		if x >= 4:
			n5 = n5+5
			paths.append(3)
		else:
			x = x-1
			x = x+7
			x = 2/x
			paths.append(4)
		paths.append(5)
		assert n5 >= 0
		d7 = n5**0.5
		return d7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))