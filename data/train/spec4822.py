import numpy as np 

def function(x):

	u8 = 7
	m9 = 2
	paths = []
	try:
		if x >= 0:
			u8 = u8*m9
			paths.append(1)
		else:
			u8 = m9/u8
			u8 = u8*2
			m9 = m9+5
			paths.append(2)
		if u8 <= 4:
			m9 = m9-u8
			paths.append(3)
		else:
			m9 = 9-6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m9 = x**0.5
		return m9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))