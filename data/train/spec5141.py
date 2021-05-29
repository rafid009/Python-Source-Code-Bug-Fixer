import numpy as np 

def function(x):

	m8 = x
	y1 = x
	x = 1
	paths = []
	try:
		if x <= 2:
			m8 = x+m8
			paths.append(1)
		else:
			y1 = 5*y1
			paths.append(2)
		if x > 9:
			y1 = 2*y1
			y1 = m8*5
			y1 = x+7
			paths.append(3)
		else:
			y1 = y1*3
			m8 = m8/y1
			x = 3*1
			paths.append(4)
		paths.append(5)
		assert y1 >= 0
		y1 = y1**0.5
		return y1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))