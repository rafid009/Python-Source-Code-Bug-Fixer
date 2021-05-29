import numpy as np 

def function(x):

	c5 = 4
	d6 = 8
	paths = []
	try:
		if d6 > 3:
			c5 = 5/d6
			c5 = c5-d6
			x = x*d6
			paths.append(1)
		else:
			c5 = c5*6
			paths.append(2)
		if d6 <= 8:
			c5 = d6+2
			d6 = d6/d6
			d6 = c5-d6
			paths.append(3)
		else:
			c5 = c5+d6
			d6 = 0*0
			x = c5*2
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