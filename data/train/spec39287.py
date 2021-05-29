import numpy as np 

def function(x):

	o7 = 7
	c5 = x
	paths = []
	try:
		if c5 < 5:
			c5 = 4+x
			x = o7*1
			x = c5/5
			paths.append(1)
		else:
			x = o7+6
			c5 = 7*1
			c5 = c5+4
			paths.append(2)
		if x <= 4:
			c5 = c5/5
			x = c5/8
			x = o7/7
			paths.append(3)
		else:
			x = 0/x
			o7 = o7*4
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