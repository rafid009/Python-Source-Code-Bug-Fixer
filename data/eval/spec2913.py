import numpy as np 

def function(x):

	f3 = 4
	d0 = x
	paths = []
	try:
		if f3 > 4:
			f3 = f3+9
			d0 = d0+2
			x = 2+x
			paths.append(1)
		else:
			d0 = d0+5
			paths.append(2)
		if d0 > 9:
			f3 = f3/3
			d0 = 1+6
			paths.append(3)
		else:
			f3 = f3-x
			d0 = d0-1
			paths.append(4)
		paths.append(5)
		assert d0 >= 0
		d0 = d0**0.5
		return d0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))