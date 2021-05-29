import numpy as np 

def function(x):

	m6 = 4
	s5 = 5
	paths = []
	try:
		if x >= 9:
			m6 = 5+5
			paths.append(1)
		else:
			x = x/1
			m6 = 0-s5
			paths.append(2)
		if x <= 8:
			s5 = 9+s5
			paths.append(3)
		else:
			m6 = m6+8
			m6 = 1/m6
			paths.append(4)
		paths.append(5)
		assert m6 >= 0
		x = m6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))