import numpy as np 

def function(x):

	c3 = 8
	d5 = x
	paths = []
	try:
		if d5 < 0:
			c3 = c3/d5
			d5 = 7/d5
			d5 = d5+7
			paths.append(1)
		else:
			c3 = 6/4
			d5 = 9*3
			paths.append(2)
		if d5 > 3:
			x = 0-0
			c3 = c3+1
			c3 = 3+c3
			paths.append(3)
		else:
			d5 = x+d5
			c3 = x*c3
			c3 = 3/x
			paths.append(4)
		paths.append(5)
		assert c3 >= 0
		d5 = c3**0.5
		return d5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))