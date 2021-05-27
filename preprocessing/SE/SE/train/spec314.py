import numpy as np 

def function(x):

	i7 = 7
	m8 = 1
	paths = []
	try:
		if m8 < 8:
			m8 = 6*m8
			m8 = x+5
			x = x/3
			paths.append(1)
		else:
			m8 = 9*m8
			m8 = 2/x
			i7 = i7-x
			paths.append(2)
		if m8 <= 6:
			x = 3/i7
			x = i7*8
			paths.append(3)
		else:
			m8 = 8+0
			paths.append(4)
		paths.append(5)
		assert m8 >= 0
		x = m8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))