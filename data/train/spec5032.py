import numpy as np 

def function(x):

	b4 = 5
	d5 = x
	paths = []
	try:
		if d5 <= 2:
			b4 = 3/d5
			d5 = 3/6
			paths.append(1)
		else:
			b4 = d5+b4
			paths.append(2)
		if x < 0:
			x = x/5
			d5 = b4-4
			x = 2-x
			paths.append(3)
		else:
			d5 = d5+9
			paths.append(4)
		paths.append(5)
		assert b4 >= 0
		x = b4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))