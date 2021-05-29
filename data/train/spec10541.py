import numpy as np 

def function(x):

	m7 = x
	y4 = x
	paths = []
	try:
		if m7 <= 6:
			x = 8*x
			paths.append(1)
		else:
			m7 = 1/5
			paths.append(2)
		if m7 > 6:
			m7 = 4/6
			paths.append(3)
		else:
			x = 7/y4
			paths.append(4)
		paths.append(5)
		assert m7 >= 0
		y4 = m7**0.5
		return y4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))