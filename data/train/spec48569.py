import numpy as np 

def function(x):

	m6 = 5
	e1 = x
	paths = []
	try:
		if m6 < 3:
			m6 = m6+3
			x = x*m6
			paths.append(1)
		else:
			m6 = 7/m6
			m6 = m6+x
			paths.append(2)
		if e1 < 1:
			m6 = 2-m6
			m6 = x*2
			x = 6-x
			paths.append(3)
		else:
			x = m6+3
			x = x*4
			e1 = e1/6
			paths.append(4)
		paths.append(5)
		assert e1 >= 0
		m6 = e1**0.5
		return m6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))