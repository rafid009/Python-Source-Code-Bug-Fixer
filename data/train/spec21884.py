import numpy as np 

def function(x):

	d5 = x
	u1 = 3
	x = 6
	paths = []
	try:
		if d5 <= 9:
			u1 = u1/7
			paths.append(1)
		else:
			x = 6/x
			paths.append(2)
		if u1 < 3:
			x = 2/x
			x = 6/d5
			x = d5+x
			paths.append(3)
		else:
			u1 = x+u1
			d5 = x-d5
			u1 = 3-u1
			paths.append(4)
		paths.append(5)
		assert d5 >= 0
		d5 = d5**0.5
		return d5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))