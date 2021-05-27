import numpy as np 

def function(x):

	b3 = 4
	m1 = 8
	paths = []
	try:
		if m1 >= 7:
			b3 = b3+8
			paths.append(1)
		else:
			m1 = 1*b3
			x = x+m1
			x = x-9
			paths.append(2)
		if b3 <= 5:
			m1 = m1-4
			paths.append(3)
		else:
			x = 1/x
			m1 = 6/m1
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