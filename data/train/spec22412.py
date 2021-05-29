import numpy as np 

def function(x):

	f5 = 0
	c8 = x
	paths = []
	try:
		if c8 <= 2:
			x = x+1
			paths.append(1)
		else:
			c8 = f5-c8
			c8 = 9/8
			paths.append(2)
		if f5 >= 7:
			f5 = x*6
			f5 = f5+8
			c8 = 4+6
			paths.append(3)
		else:
			f5 = c8*4
			paths.append(4)
		paths.append(5)
		assert c8 >= 0
		f5 = c8**0.5
		return f5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))