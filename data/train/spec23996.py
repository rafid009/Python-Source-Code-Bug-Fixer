import numpy as np 

def function(x):

	i6 = 6
	d2 = 1
	paths = []
	try:
		if x <= 1:
			d2 = 4*2
			d2 = i6*3
			paths.append(1)
		else:
			d2 = 2+x
			paths.append(2)
		if i6 > 0:
			i6 = 6+i6
			paths.append(3)
		else:
			d2 = 4-1
			x = x-x
			x = x+i6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))