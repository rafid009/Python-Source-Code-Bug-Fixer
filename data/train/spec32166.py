import numpy as np 

def function(x):

	c7 = x
	d2 = x
	paths = []
	try:
		if d2 > 6:
			x = x/8
			x = 5/x
			c7 = c7+d2
			paths.append(1)
		else:
			c7 = 5*0
			x = x/3
			paths.append(2)
		if d2 < 7:
			d2 = d2*2
			c7 = c7-x
			paths.append(3)
		else:
			d2 = 5-2
			c7 = 1*4
			paths.append(4)
		paths.append(5)
		assert c7 >= 0
		x = c7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))