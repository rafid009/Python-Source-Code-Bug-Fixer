import numpy as np 

def function(x):

	i4 = x
	d7 = 1
	x = x
	paths = []
	try:
		if x >= 9:
			i4 = i4/2
			paths.append(1)
		else:
			d7 = 2/7
			x = x*x
			paths.append(2)
		if i4 < 8:
			d7 = 6+d7
			paths.append(3)
		else:
			i4 = 0*i4
			x = 0/x
			d7 = d7*x
			paths.append(4)
		paths.append(5)
		assert i4 >= 0
		i4 = i4**0.5
		return i4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))