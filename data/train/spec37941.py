import numpy as np 

def function(x):

	m0 = x
	l5 = 0
	paths = []
	try:
		if x > 4:
			x = l5*5
			l5 = 1/m0
			l5 = l5-5
			paths.append(1)
		else:
			l5 = x+7
			paths.append(2)
		if l5 < 5:
			l5 = l5*x
			m0 = m0+0
			paths.append(3)
		else:
			x = 4+x
			x = 4/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m0 = x**0.5
		return m0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))