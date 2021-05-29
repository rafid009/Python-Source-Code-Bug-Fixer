import numpy as np 

def function(x):

	r9 = 4
	d7 = x
	paths = []
	try:
		if x > 9:
			d7 = 3-d7
			paths.append(1)
		else:
			d7 = r9-1
			x = x*0
			r9 = r9/4
			paths.append(2)
		if x <= 6:
			r9 = 6/r9
			paths.append(3)
		else:
			x = x+9
			r9 = 8/r9
			paths.append(4)
		paths.append(5)
		assert d7 >= 0
		d7 = d7**0.5
		return d7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))