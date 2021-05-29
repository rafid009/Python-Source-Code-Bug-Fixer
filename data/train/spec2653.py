import numpy as np 

def function(x):

	n4 = x
	d7 = x
	x = 1
	paths = []
	try:
		if d7 > 2:
			d7 = d7/6
			n4 = n4/9
			paths.append(1)
		else:
			d7 = d7+3
			x = 7+x
			n4 = n4+2
			paths.append(2)
		if x <= 3:
			d7 = 7+d7
			x = d7-7
			d7 = n4*2
			paths.append(3)
		else:
			x = 8/3
			n4 = x/x
			paths.append(4)
		paths.append(5)
		assert d7 >= 0
		x = d7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))