import numpy as np 

def function(x):

	m4 = x
	b0 = 3
	paths = []
	try:
		if m4 >= 8:
			x = 8/4
			m4 = m4*1
			m4 = m4-5
			paths.append(1)
		else:
			m4 = m4/1
			b0 = 6-b0
			paths.append(2)
		if x > 8:
			x = 1/x
			m4 = 7+m4
			b0 = 0-b0
			paths.append(3)
		else:
			b0 = m4/b0
			paths.append(4)
		paths.append(5)
		assert b0 >= 0
		m4 = b0**0.5
		return m4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))