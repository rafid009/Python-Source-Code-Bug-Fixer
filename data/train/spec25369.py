import numpy as np 

def function(x):

	m9 = x
	b4 = 1
	x = 1
	paths = []
	try:
		if b4 >= 6:
			x = b4+x
			b4 = b4/b4
			m9 = m9*2
			paths.append(1)
		else:
			x = m9-6
			m9 = 1/1
			paths.append(2)
		if m9 < 2:
			b4 = 9+b4
			paths.append(3)
		else:
			x = 1/m9
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