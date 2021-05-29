import numpy as np 

def function(x):

	u9 = x
	d0 = 5
	paths = []
	try:
		if u9 >= 3:
			d0 = 0-3
			x = 4/d0
			paths.append(1)
		else:
			d0 = d0/1
			paths.append(2)
		if u9 >= 0:
			x = x-5
			paths.append(3)
		else:
			d0 = 1+u9
			paths.append(4)
		paths.append(5)
		assert u9 >= 0
		d0 = u9**0.5
		return d0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))