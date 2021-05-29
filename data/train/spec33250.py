import numpy as np 

def function(x):

	c8 = 2
	b9 = x
	paths = []
	try:
		if x > 2:
			x = 4-x
			paths.append(1)
		else:
			c8 = x*2
			b9 = 3*8
			paths.append(2)
		if c8 < 0:
			c8 = c8+x
			b9 = 8/9
			paths.append(3)
		else:
			x = c8+x
			x = x*8
			paths.append(4)
		paths.append(5)
		assert c8 >= 0
		b9 = c8**0.5
		return b9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))