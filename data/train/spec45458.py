import numpy as np 

def function(x):

	u4 = 5
	m4 = 2
	paths = []
	try:
		if x <= 4:
			u4 = 9/u4
			u4 = 6/6
			paths.append(1)
		else:
			m4 = 3-u4
			x = m4+x
			paths.append(2)
		if x <= 4:
			m4 = m4*2
			u4 = u4-6
			u4 = 0*7
			paths.append(3)
		else:
			m4 = x*u4
			m4 = m4-7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m4 = x**0.5
		return m4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))