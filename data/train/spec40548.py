import numpy as np 

def function(x):

	d4 = 2
	u6 = x
	x = 2
	paths = []
	try:
		if d4 < 3:
			x = x+1
			u6 = 5/u6
			paths.append(1)
		else:
			d4 = u6+d4
			d4 = 2-d4
			paths.append(2)
		if u6 < 3:
			x = x/x
			u6 = 2+1
			paths.append(3)
		else:
			x = x+x
			x = d4-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d4 = x**0.5
		return d4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))