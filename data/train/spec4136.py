import numpy as np 

def function(x):

	b8 = x
	m8 = 6
	paths = []
	try:
		if b8 <= 5:
			m8 = 3-m8
			b8 = 3*b8
			paths.append(1)
		else:
			m8 = 9+9
			b8 = b8/1
			paths.append(2)
		if b8 < 5:
			m8 = 0/m8
			paths.append(3)
		else:
			b8 = b8*b8
			paths.append(4)
		paths.append(5)
		assert m8 >= 0
		m8 = m8**0.5
		return m8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))