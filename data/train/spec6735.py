import numpy as np 

def function(x):

	c6 = 6
	m7 = x
	paths = []
	try:
		if c6 < 2:
			x = 3-9
			x = 0/x
			m7 = 5+m7
			paths.append(1)
		else:
			c6 = c6-m7
			x = x/6
			x = x/3
			paths.append(2)
		if x < 6:
			c6 = m7+x
			m7 = 6*m7
			paths.append(3)
		else:
			x = x-6
			c6 = c6-2
			c6 = c6+x
			paths.append(4)
		paths.append(5)
		assert c6 >= 0
		x = c6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))