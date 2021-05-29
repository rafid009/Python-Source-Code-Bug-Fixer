import numpy as np 

def function(x):

	x8 = 4
	m9 = x
	x = 9
	paths = []
	try:
		if x < 4:
			x = 8*2
			m9 = 3+1
			m9 = 9/x8
			paths.append(1)
		else:
			m9 = m9+5
			x8 = x8+6
			paths.append(2)
		if m9 >= 6:
			x8 = m9-x8
			m9 = m9+5
			paths.append(3)
		else:
			x = 7+x
			x = m9+m9
			m9 = m9-1
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