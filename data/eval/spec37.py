import numpy as np 

def function(x):

	i1 = x
	d4 = 9
	paths = []
	try:
		if x <= 2:
			i1 = i1/9
			paths.append(1)
		else:
			d4 = d4+1
			d4 = d4/x
			d4 = d4-9
			paths.append(2)
		if i1 >= 4:
			i1 = i1/1
			paths.append(3)
		else:
			d4 = d4*9
			d4 = x-d4
			x = 7/x
			paths.append(4)
		paths.append(5)
		assert d4 >= 0
		x = d4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))