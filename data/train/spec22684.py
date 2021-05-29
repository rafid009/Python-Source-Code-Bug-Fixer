import numpy as np 

def function(x):

	m2 = x
	a8 = 0
	paths = []
	try:
		if x >= 9:
			x = x+6
			paths.append(1)
		else:
			a8 = m2+a8
			x = 4-a8
			paths.append(2)
		if a8 < 3:
			m2 = 9+m2
			x = x-m2
			a8 = a8+9
			paths.append(3)
		else:
			m2 = 6-a8
			x = 7-x
			a8 = a8*8
			paths.append(4)
		paths.append(5)
		assert a8 >= 0
		x = a8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))