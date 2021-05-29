import numpy as np 

def function(x):

	c5 = x
	m3 = 1
	x = 3
	paths = []
	try:
		if x > 1:
			m3 = x/5
			m3 = c5-m3
			x = x-m3
			paths.append(1)
		else:
			m3 = x/m3
			x = 9*3
			paths.append(2)
		if c5 > 4:
			m3 = m3-x
			x = m3+6
			x = x/3
			paths.append(3)
		else:
			c5 = 2*c5
			m3 = m3+7
			paths.append(4)
		paths.append(5)
		assert m3 >= 0
		x = m3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))