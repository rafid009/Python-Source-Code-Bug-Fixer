import numpy as np 

def function(x):

	h8 = x
	m8 = x
	paths = []
	try:
		if x < 0:
			h8 = h8*6
			h8 = 8+1
			paths.append(1)
		else:
			m8 = 5+x
			paths.append(2)
		if m8 >= 6:
			h8 = 6-1
			m8 = 7*m8
			paths.append(3)
		else:
			m8 = m8+h8
			h8 = 0-h8
			paths.append(4)
		paths.append(5)
		assert h8 >= 0
		m8 = h8**0.5
		return m8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))