import numpy as np 

def function(x):

	d5 = 6
	o2 = 6
	paths = []
	try:
		if d5 > 6:
			d5 = d5-5
			x = o2+3
			x = x-x
			paths.append(1)
		else:
			d5 = x*6
			paths.append(2)
		if o2 <= 5:
			d5 = d5/2
			x = 5*x
			paths.append(3)
		else:
			x = 9+6
			d5 = d5*1
			o2 = 9/3
			paths.append(4)
		paths.append(5)
		assert d5 >= 0
		x = d5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))