import numpy as np 

def function(x):

	u8 = x
	c5 = x
	paths = []
	try:
		if c5 > 7:
			x = c5-x
			paths.append(1)
		else:
			x = 7*x
			c5 = x*8
			x = x*0
			paths.append(2)
		if x <= 5:
			c5 = 7*c5
			c5 = c5+3
			paths.append(3)
		else:
			u8 = u8/7
			c5 = u8+4
			paths.append(4)
		paths.append(5)
		assert u8 >= 0
		x = u8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))