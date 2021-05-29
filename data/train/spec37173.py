import numpy as np 

def function(x):

	m4 = 8
	i0 = x
	paths = []
	try:
		if m4 > 1:
			i0 = 3*7
			m4 = m4*9
			x = x/7
			paths.append(1)
		else:
			m4 = m4+7
			x = x+i0
			paths.append(2)
		if i0 > 2:
			m4 = x+m4
			paths.append(3)
		else:
			x = 8-m4
			x = i0*x
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