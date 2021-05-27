import numpy as np 

def function(x):

	l0 = x
	m5 = 9
	paths = []
	try:
		if x < 9:
			m5 = 0*x
			l0 = m5*l0
			paths.append(1)
		else:
			l0 = 2*l0
			x = x-8
			paths.append(2)
		if x <= 0:
			l0 = l0-9
			x = 4+x
			paths.append(3)
		else:
			m5 = m5-4
			paths.append(4)
		paths.append(5)
		assert l0 >= 0
		m5 = l0**0.5
		return m5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))