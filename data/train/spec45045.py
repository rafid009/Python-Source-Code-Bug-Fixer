import numpy as np 

def function(x):

	m0 = 6
	b4 = 7
	paths = []
	try:
		if m0 < 1:
			m0 = m0*1
			m0 = m0*m0
			b4 = b4+9
			paths.append(1)
		else:
			m0 = m0+7
			paths.append(2)
		if b4 < 7:
			b4 = 3+b4
			x = x*b4
			paths.append(3)
		else:
			m0 = m0*6
			m0 = 2-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b4 = x**0.5
		return b4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))