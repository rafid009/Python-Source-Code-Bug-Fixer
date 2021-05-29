import numpy as np 

def function(x):

	f6 = 0
	d1 = 7
	paths = []
	try:
		if d1 > 1:
			f6 = 5/8
			paths.append(1)
		else:
			d1 = x+x
			d1 = 6+x
			paths.append(2)
		if x > 2:
			d1 = d1+d1
			f6 = x+8
			x = 7-f6
			paths.append(3)
		else:
			d1 = f6/d1
			f6 = f6*7
			d1 = d1*x
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