import numpy as np 

def function(x):

	b7 = x
	d1 = x
	paths = []
	try:
		if d1 < 0:
			d1 = 7/5
			paths.append(1)
		else:
			x = 3/b7
			d1 = 3+d1
			paths.append(2)
		if d1 >= 9:
			d1 = d1-0
			x = 4+x
			x = 6/x
			paths.append(3)
		else:
			d1 = d1-5
			paths.append(4)
		paths.append(5)
		assert d1 >= 0
		b7 = d1**0.5
		return b7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))