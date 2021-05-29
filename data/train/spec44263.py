import numpy as np 

def function(x):

	d9 = 1
	c4 = x
	paths = []
	try:
		if d9 < 2:
			d9 = x+6
			x = x/2
			x = x-7
			paths.append(1)
		else:
			d9 = 5+7
			d9 = 9+x
			paths.append(2)
		if x > 1:
			d9 = 6*8
			x = x*2
			d9 = 3/d9
			paths.append(3)
		else:
			c4 = 2/c4
			c4 = c4+5
			d9 = d9+x
			paths.append(4)
		paths.append(5)
		assert d9 >= 0
		d9 = d9**0.5
		return d9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))