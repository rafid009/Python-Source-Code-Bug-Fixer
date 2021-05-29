import numpy as np 

def function(x):

	m5 = x
	m3 = x
	paths = []
	try:
		if m5 >= 3:
			x = m3*5
			x = x+4
			paths.append(1)
		else:
			m3 = 2*m3
			x = x+m5
			m5 = 3-6
			paths.append(2)
		if m5 < 9:
			m5 = 0/5
			paths.append(3)
		else:
			m3 = m3/m5
			m5 = 0+6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m3 = x**0.5
		return m3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))