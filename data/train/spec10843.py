import numpy as np 

def function(x):

	m6 = x
	f2 = 4
	paths = []
	try:
		if x > 2:
			x = 0-5
			m6 = 1-7
			f2 = 7*f2
			paths.append(1)
		else:
			m6 = m6-0
			f2 = f2-x
			f2 = 6+8
			paths.append(2)
		if x < 2:
			m6 = 2*m6
			f2 = 3-f2
			f2 = x*1
			paths.append(3)
		else:
			f2 = 5/9
			m6 = m6-2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m6 = x**0.5
		return m6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))