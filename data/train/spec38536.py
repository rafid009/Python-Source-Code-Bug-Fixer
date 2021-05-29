import numpy as np 

def function(x):

	m7 = x
	c8 = 1
	paths = []
	try:
		if c8 > 3:
			c8 = c8-m7
			paths.append(1)
		else:
			x = x/2
			paths.append(2)
		if m7 < 4:
			x = c8*9
			m7 = x-7
			paths.append(3)
		else:
			c8 = 0-c8
			paths.append(4)
		paths.append(5)
		assert c8 >= 0
		x = c8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))