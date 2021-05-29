import numpy as np 

def function(x):

	f4 = 7
	m7 = x
	paths = []
	try:
		if f4 < 1:
			f4 = f4*4
			m7 = m7/1
			paths.append(1)
		else:
			f4 = f4-8
			f4 = 3+m7
			paths.append(2)
		if x >= 3:
			m7 = 3*f4
			paths.append(3)
		else:
			m7 = f4*x
			m7 = x-5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m7 = x**0.5
		return m7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))