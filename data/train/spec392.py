import numpy as np 

def function(x):

	f7 = 3
	m0 = 7
	paths = []
	try:
		if x >= 1:
			m0 = 7*m0
			x = x*x
			m0 = m0+4
			paths.append(1)
		else:
			m0 = 9*m0
			m0 = f7+m0
			f7 = f7+9
			paths.append(2)
		if f7 >= 9:
			m0 = m0*x
			paths.append(3)
		else:
			x = x*8
			m0 = 4+5
			m0 = m0+7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))