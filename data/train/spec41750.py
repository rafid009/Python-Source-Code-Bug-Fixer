import numpy as np 

def function(x):

	d9 = 3
	u1 = 8
	paths = []
	try:
		if x <= 9:
			d9 = d9/7
			u1 = u1*x
			paths.append(1)
		else:
			u1 = u1-1
			paths.append(2)
		if u1 > 3:
			d9 = d9*3
			x = 2+x
			u1 = 2/u1
			paths.append(3)
		else:
			d9 = 9/1
			d9 = d9*6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))