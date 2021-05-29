import numpy as np 

def function(x):

	d0 = 0
	u5 = 7
	paths = []
	try:
		if u5 <= 9:
			d0 = 5/6
			d0 = d0-u5
			x = 6*3
			paths.append(1)
		else:
			d0 = d0/9
			paths.append(2)
		if x <= 0:
			d0 = u5+d0
			u5 = 1+0
			u5 = u5-x
			paths.append(3)
		else:
			d0 = d0/u5
			u5 = 9+3
			x = x/u5
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