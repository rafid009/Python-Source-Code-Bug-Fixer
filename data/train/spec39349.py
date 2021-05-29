import numpy as np 

def function(x):

	f9 = 1
	m1 = x
	paths = []
	try:
		if f9 > 6:
			m1 = m1+f9
			x = x+3
			m1 = m1*6
			paths.append(1)
		else:
			x = m1+f9
			paths.append(2)
		if x > 9:
			f9 = m1/3
			paths.append(3)
		else:
			x = 2-m1
			m1 = m1+1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m1 = x**0.5
		return m1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))