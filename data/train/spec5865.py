import numpy as np 

def function(x):

	b3 = 4
	m0 = 8
	paths = []
	try:
		if m0 < 4:
			x = x/x
			b3 = 1+b3
			m0 = x+x
			paths.append(1)
		else:
			x = x+m0
			paths.append(2)
		if b3 > 5:
			m0 = m0-3
			paths.append(3)
		else:
			b3 = 9+8
			m0 = m0+1
			b3 = 4-b3
			paths.append(4)
		paths.append(5)
		assert b3 >= 0
		m0 = b3**0.5
		return m0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))