import numpy as np 

def function(x):

	d2 = 1
	i4 = x
	paths = []
	try:
		if x < 7:
			i4 = i4-6
			d2 = x+4
			paths.append(1)
		else:
			i4 = x/i4
			x = 7*x
			paths.append(2)
		if i4 >= 2:
			d2 = i4*d2
			x = i4+x
			i4 = 9*i4
			paths.append(3)
		else:
			d2 = 3/d2
			d2 = d2/i4
			paths.append(4)
		paths.append(5)
		assert d2 >= 0
		i4 = d2**0.5
		return i4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))