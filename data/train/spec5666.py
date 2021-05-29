import numpy as np 

def function(x):

	d1 = x
	o1 = x
	paths = []
	try:
		if d1 >= 0:
			x = 3*x
			paths.append(1)
		else:
			x = x*o1
			d1 = 1+o1
			d1 = d1*2
			paths.append(2)
		if d1 > 4:
			x = 4*7
			o1 = 3+x
			x = 4/x
			paths.append(3)
		else:
			d1 = 2*d1
			o1 = 2+9
			paths.append(4)
		paths.append(5)
		assert d1 >= 0
		d1 = d1**0.5
		return d1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))