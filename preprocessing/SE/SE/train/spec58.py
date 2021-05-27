import numpy as np 

def function(x):

	m0 = 1
	u4 = 6
	paths = []
	try:
		if u4 > 3:
			m0 = 3*m0
			u4 = 9/8
			m0 = m0-m0
			paths.append(1)
		else:
			m0 = 8*m0
			u4 = u4*8
			m0 = m0+3
			paths.append(2)
		if m0 <= 2:
			m0 = m0-m0
			m0 = x-6
			u4 = 6-9
			paths.append(3)
		else:
			m0 = 2/u4
			paths.append(4)
		paths.append(5)
		assert m0 >= 0
		u4 = m0**0.5
		return u4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))