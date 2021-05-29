import numpy as np 

def function(x):

	e4 = x
	m5 = 5
	paths = []
	try:
		if m5 >= 6:
			m5 = m5/5
			e4 = e4/3
			paths.append(1)
		else:
			e4 = e4/2
			x = 8*x
			x = x*e4
			paths.append(2)
		if m5 < 8:
			m5 = m5+5
			m5 = m5-e4
			paths.append(3)
		else:
			m5 = 4/5
			e4 = e4+e4
			paths.append(4)
		paths.append(5)
		assert e4 >= 0
		m5 = e4**0.5
		return m5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))