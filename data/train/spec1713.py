import numpy as np 

def function(x):

	u4 = x
	m7 = x
	paths = []
	try:
		if u4 >= 2:
			m7 = x/m7
			m7 = 3/m7
			x = 4-x
			paths.append(1)
		else:
			u4 = 1-u4
			u4 = u4+u4
			u4 = 6/4
			paths.append(2)
		if u4 >= 5:
			u4 = 4/5
			paths.append(3)
		else:
			x = x/5
			m7 = m7-8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))