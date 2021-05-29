import numpy as np 

def function(x):

	c3 = 4
	o1 = 7
	paths = []
	try:
		if o1 > 4:
			c3 = 7-9
			paths.append(1)
		else:
			o1 = 9*o1
			paths.append(2)
		if c3 >= 0:
			c3 = 4*c3
			o1 = o1*0
			paths.append(3)
		else:
			c3 = c3/o1
			o1 = x+x
			paths.append(4)
		paths.append(5)
		assert o1 >= 0
		x = o1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))