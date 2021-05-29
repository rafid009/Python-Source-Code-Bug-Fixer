import numpy as np 

def function(x):

	m8 = x
	p9 = 5
	paths = []
	try:
		if x > 1:
			m8 = 0-m8
			paths.append(1)
		else:
			m8 = x+1
			paths.append(2)
		if x >= 1:
			p9 = p9+x
			m8 = 2/m8
			paths.append(3)
		else:
			p9 = p9*8
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