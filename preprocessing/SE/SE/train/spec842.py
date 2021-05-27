import numpy as np 

def function(x):

	m7 = 6
	c4 = x
	paths = []
	try:
		if x > 3:
			x = 0-5
			m7 = 4-m7
			x = 9+c4
			paths.append(1)
		else:
			x = 2/6
			x = x+2
			c4 = c4+8
			paths.append(2)
		if x > 5:
			x = 9/x
			m7 = m7-1
			paths.append(3)
		else:
			m7 = 9+m7
			paths.append(4)
		paths.append(5)
		assert c4 >= 0
		x = c4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))