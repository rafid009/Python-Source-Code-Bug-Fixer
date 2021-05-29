import numpy as np 

def function(x):

	i0 = 0
	d9 = 4
	paths = []
	try:
		if i0 < 8:
			i0 = 3+7
			i0 = i0+1
			d9 = d9-9
			paths.append(1)
		else:
			i0 = 2-1
			paths.append(2)
		if i0 >= 5:
			x = x*d9
			d9 = i0*d9
			paths.append(3)
		else:
			i0 = x/7
			d9 = d9+2
			paths.append(4)
		paths.append(5)
		assert d9 >= 0
		x = d9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))