import numpy as np 

def function(x):

	m0 = x
	l0 = x
	x = x
	paths = []
	try:
		if l0 > 3:
			l0 = x*l0
			x = l0*4
			paths.append(1)
		else:
			l0 = 1/l0
			paths.append(2)
		if m0 > 6:
			m0 = 3*m0
			l0 = l0-5
			paths.append(3)
		else:
			m0 = 6/m0
			m0 = m0/2
			x = 1+x
			paths.append(4)
		paths.append(5)
		assert m0 >= 0
		x = m0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))