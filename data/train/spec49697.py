import numpy as np 

def function(x):

	f3 = 2
	d6 = x
	paths = []
	try:
		if x < 0:
			f3 = 1+f3
			f3 = f3*d6
			paths.append(1)
		else:
			x = f3+f3
			x = 6+1
			d6 = d6*f3
			paths.append(2)
		if f3 < 6:
			f3 = 6+6
			x = x-1
			x = 2+f3
			paths.append(3)
		else:
			x = x/x
			d6 = 4*3
			d6 = 3+f3
			paths.append(4)
		paths.append(5)
		assert d6 >= 0
		d6 = d6**0.5
		return d6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))