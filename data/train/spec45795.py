import numpy as np 

def function(x):

	d9 = 6
	x6 = x
	paths = []
	try:
		if d9 >= 7:
			x6 = x6*6
			paths.append(1)
		else:
			d9 = x/4
			x = x-d9
			x6 = x6*x
			paths.append(2)
		if x6 > 5:
			x = 3+x
			x = x*8
			d9 = 2/d9
			paths.append(3)
		else:
			x = x*x
			d9 = 6/8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d9 = x**0.5
		return d9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))