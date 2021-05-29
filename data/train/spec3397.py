import numpy as np 

def function(x):

	f2 = 9
	m4 = x
	paths = []
	try:
		if x >= 8:
			f2 = m4*m4
			paths.append(1)
		else:
			f2 = f2+x
			x = m4+x
			f2 = m4-4
			paths.append(2)
		if m4 < 3:
			m4 = 6-1
			f2 = f2*5
			paths.append(3)
		else:
			m4 = m4+2
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