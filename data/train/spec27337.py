import numpy as np 

def function(x):

	d7 = x
	r3 = 3
	paths = []
	try:
		if d7 <= 3:
			d7 = d7*1
			d7 = d7+1
			paths.append(1)
		else:
			x = x-9
			d7 = r3-x
			r3 = d7/8
			paths.append(2)
		if x < 0:
			x = 3/x
			r3 = 8*r3
			paths.append(3)
		else:
			d7 = r3*r3
			r3 = 9*6
			d7 = 3+1
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