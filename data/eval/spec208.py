import numpy as np 

def function(x):

	m4 = 5
	y4 = x
	paths = []
	try:
		if x <= 5:
			y4 = y4/x
			y4 = y4*2
			paths.append(1)
		else:
			m4 = y4-7
			paths.append(2)
		if x > 0:
			m4 = x+8
			paths.append(3)
		else:
			y4 = y4-9
			paths.append(4)
		paths.append(5)
		assert y4 >= 0
		m4 = y4**0.5
		return m4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))