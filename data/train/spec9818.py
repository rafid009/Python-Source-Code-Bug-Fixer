import numpy as np 

def function(x):

	o2 = 8
	c8 = 8
	paths = []
	try:
		if x <= 2:
			x = 2+x
			paths.append(1)
		else:
			c8 = 2/c8
			c8 = 2+0
			paths.append(2)
		if x > 8:
			o2 = o2+1
			c8 = 4+9
			paths.append(3)
		else:
			c8 = o2*3
			c8 = x*o2
			c8 = 8-c8
			paths.append(4)
		paths.append(5)
		assert c8 >= 0
		o2 = c8**0.5
		return o2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))