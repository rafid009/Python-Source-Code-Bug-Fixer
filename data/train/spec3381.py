import numpy as np 

def function(x):

	m2 = 9
	y1 = x
	paths = []
	try:
		if x < 0:
			m2 = 1*m2
			m2 = 4/y1
			m2 = m2-2
			paths.append(1)
		else:
			m2 = 7+y1
			x = 1/m2
			paths.append(2)
		if x > 6:
			y1 = 6+3
			x = x+7
			paths.append(3)
		else:
			x = 5/x
			m2 = m2-x
			x = m2*x
			paths.append(4)
		paths.append(5)
		assert y1 >= 0
		x = y1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))