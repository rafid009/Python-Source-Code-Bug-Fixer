import numpy as np 

def function(x):

	e8 = 0
	m1 = x
	paths = []
	try:
		if m1 < 8:
			x = 5*x
			m1 = 1-m1
			e8 = e8+1
			paths.append(1)
		else:
			x = 4-x
			x = 1+x
			paths.append(2)
		if e8 > 6:
			x = x-1
			m1 = 0-m1
			x = e8*e8
			paths.append(3)
		else:
			x = x/5
			e8 = m1-7
			paths.append(4)
		paths.append(5)
		assert m1 >= 0
		m1 = m1**0.5
		return m1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))