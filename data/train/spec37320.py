import numpy as np 

def function(x):

	m2 = 4
	c5 = x
	x = 4
	paths = []
	try:
		if m2 <= 4:
			x = x/4
			c5 = 3+c5
			c5 = 2/c5
			paths.append(1)
		else:
			x = 1/x
			paths.append(2)
		if x <= 4:
			c5 = c5-5
			c5 = c5*9
			m2 = m2/6
			paths.append(3)
		else:
			c5 = c5-c5
			m2 = c5/m2
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