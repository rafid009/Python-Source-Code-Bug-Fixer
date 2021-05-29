import numpy as np 

def function(x):

	m8 = 5
	e8 = 2
	x = x
	paths = []
	try:
		if m8 < 2:
			m8 = m8*e8
			m8 = 5+3
			m8 = 5/m8
			paths.append(1)
		else:
			e8 = e8/x
			x = x/4
			paths.append(2)
		if x <= 6:
			e8 = e8+m8
			e8 = e8/e8
			paths.append(3)
		else:
			x = 7*1
			m8 = e8+4
			x = 3*0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m8 = x**0.5
		return m8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))