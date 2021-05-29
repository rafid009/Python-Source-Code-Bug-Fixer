import numpy as np 

def function(x):

	d0 = x
	f5 = 0
	paths = []
	try:
		if x >= 6:
			f5 = d0+x
			x = 1+1
			paths.append(1)
		else:
			d0 = 9+d0
			f5 = 2+2
			f5 = 5-f5
			paths.append(2)
		if f5 >= 5:
			f5 = f5-2
			d0 = 3+d0
			paths.append(3)
		else:
			f5 = 2-f5
			x = x/x
			paths.append(4)
		paths.append(5)
		assert d0 >= 0
		x = d0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))