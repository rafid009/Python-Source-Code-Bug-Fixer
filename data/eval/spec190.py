import numpy as np 

def function(x):

	m1 = x
	q8 = 4
	paths = []
	try:
		if m1 <= 2:
			m1 = x/5
			m1 = 1+8
			m1 = m1-m1
			paths.append(1)
		else:
			x = 3+0
			m1 = x+m1
			paths.append(2)
		if q8 <= 9:
			x = 2-x
			q8 = 1+q8
			paths.append(3)
		else:
			x = x/2
			x = 2-8
			q8 = q8+9
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