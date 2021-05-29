import numpy as np 

def function(x):

	m3 = x
	y3 = 7
	x = x
	paths = []
	try:
		if m3 <= 3:
			y3 = 0-y3
			y3 = y3-6
			paths.append(1)
		else:
			y3 = y3/x
			y3 = 0/y3
			x = 7*9
			paths.append(2)
		if m3 <= 6:
			y3 = 7+m3
			paths.append(3)
		else:
			m3 = m3+3
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