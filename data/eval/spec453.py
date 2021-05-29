import numpy as np 

def function(x):

	m4 = x
	paths = []
	try:
		if m4 >= 9:
			m4 = m4+m4
			paths.append(1)
		else:
			m4 = m4/1
			m4 = 8/m4
			paths.append(2)
		if x > 1:
			m4 = m4/5
			paths.append(3)
		else:
			m4 = 7-m4
			x = x+0
			paths.append(4)
		paths.append(5)
		assert m4 >= 0
		m4 = m4**0.5
		return m4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))