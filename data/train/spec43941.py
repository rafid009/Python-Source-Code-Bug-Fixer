import numpy as np 

def function(x):

	f0 = 0
	d0 = x
	paths = []
	try:
		if f0 > 6:
			f0 = 1-f0
			d0 = d0/8
			x = d0+x
			paths.append(1)
		else:
			d0 = 9*d0
			paths.append(2)
		if d0 < 5:
			d0 = f0/8
			paths.append(3)
		else:
			x = x*1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f0 = x**0.5
		return f0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))