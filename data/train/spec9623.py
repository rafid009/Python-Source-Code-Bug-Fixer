import numpy as np 

def function(x):

	x4 = x
	m5 = 5
	paths = []
	try:
		if x4 > 0:
			m5 = 9+5
			paths.append(1)
		else:
			x = 4-x
			paths.append(2)
		if x4 >= 3:
			x4 = 7/7
			x = 0+x4
			x = 4/8
			paths.append(3)
		else:
			m5 = x4*m5
			x4 = 7+x4
			x = 0*x
			paths.append(4)
		paths.append(5)
		assert m5 >= 0
		x4 = m5**0.5
		return x4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))