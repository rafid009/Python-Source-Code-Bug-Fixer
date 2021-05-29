import numpy as np 

def function(x):

	b2 = x
	m6 = x
	paths = []
	try:
		if b2 <= 0:
			x = 1+2
			m6 = 9/9
			paths.append(1)
		else:
			b2 = 5*x
			paths.append(2)
		if x >= 7:
			m6 = m6+3
			x = x/6
			paths.append(3)
		else:
			b2 = 7-b2
			paths.append(4)
		paths.append(5)
		assert b2 >= 0
		m6 = b2**0.5
		return m6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))