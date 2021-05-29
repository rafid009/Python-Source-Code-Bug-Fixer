import numpy as np 

def function(x):

	o3 = 5
	c5 = x
	paths = []
	try:
		if x <= 2:
			o3 = 9-o3
			paths.append(1)
		else:
			x = 8/6
			x = x+0
			x = x+1
			paths.append(2)
		if c5 > 0:
			c5 = o3/3
			o3 = c5-8
			c5 = x*c5
			paths.append(3)
		else:
			x = 3*x
			c5 = 2-o3
			paths.append(4)
		paths.append(5)
		assert c5 >= 0
		x = c5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))