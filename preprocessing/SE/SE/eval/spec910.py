import numpy as np 

def function(x):

	f2 = x
	d1 = x
	paths = []
	try:
		if f2 >= 3:
			x = x-1
			d1 = f2/d1
			paths.append(1)
		else:
			f2 = f2-x
			f2 = f2*9
			paths.append(2)
		if d1 >= 4:
			d1 = d1*2
			d1 = d1/x
			x = x/5
			paths.append(3)
		else:
			d1 = f2+d1
			d1 = 2*d1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d1 = x**0.5
		return d1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))