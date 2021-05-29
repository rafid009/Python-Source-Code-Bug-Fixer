import numpy as np 

def function(x):

	r7 = 5
	m0 = x
	paths = []
	try:
		if m0 < 7:
			x = 4/x
			r7 = x+1
			paths.append(1)
		else:
			m0 = m0-6
			x = r7*x
			x = 5/7
			paths.append(2)
		if x <= 2:
			r7 = x/r7
			x = x+1
			paths.append(3)
		else:
			r7 = x+m0
			m0 = m0-x
			r7 = 1-6
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