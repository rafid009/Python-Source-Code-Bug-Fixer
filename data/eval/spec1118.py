import numpy as np 

def function(x):

	d1 = x
	i9 = x
	paths = []
	try:
		if i9 <= 8:
			i9 = i9*1
			d1 = 5*d1
			i9 = 1/i9
			paths.append(1)
		else:
			i9 = i9*3
			paths.append(2)
		if d1 < 5:
			x = 8*x
			x = 2/3
			i9 = i9+2
			paths.append(3)
		else:
			d1 = 5-d1
			i9 = i9*2
			paths.append(4)
		paths.append(5)
		assert d1 >= 0
		x = d1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))