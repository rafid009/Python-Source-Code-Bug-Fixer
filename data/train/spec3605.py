import numpy as np 

def function(x):

	y8 = 9
	m9 = x
	paths = []
	try:
		if y8 <= 1:
			x = m9-x
			paths.append(1)
		else:
			x = 2+5
			y8 = m9-1
			y8 = y8*7
			paths.append(2)
		if y8 >= 7:
			m9 = 5-m9
			paths.append(3)
		else:
			y8 = y8-9
			paths.append(4)
		paths.append(5)
		assert m9 >= 0
		x = m9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))