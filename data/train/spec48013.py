import numpy as np 

def function(x):

	m7 = 1
	y7 = x
	x = x
	paths = []
	try:
		if x < 6:
			m7 = m7*m7
			m7 = 2-m7
			y7 = y7+2
			paths.append(1)
		else:
			y7 = y7/x
			paths.append(2)
		if m7 >= 1:
			x = 4-x
			paths.append(3)
		else:
			x = x/9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y7 = x**0.5
		return y7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))