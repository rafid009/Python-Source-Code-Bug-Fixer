import numpy as np 

def function(x):

	y8 = x
	m4 = x
	paths = []
	try:
		if x > 1:
			m4 = m4+y8
			x = x+x
			paths.append(1)
		else:
			m4 = 8/2
			x = m4*9
			y8 = 2-y8
			paths.append(2)
		if y8 < 4:
			m4 = 2/3
			paths.append(3)
		else:
			y8 = y8-5
			x = 6-x
			paths.append(4)
		paths.append(5)
		assert y8 >= 0
		y8 = y8**0.5
		return y8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))