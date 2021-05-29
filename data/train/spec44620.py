import numpy as np 

def function(x):

	m3 = 3
	h9 = 6
	paths = []
	try:
		if h9 >= 7:
			m3 = 2+8
			h9 = h9*1
			paths.append(1)
		else:
			m3 = m3*7
			paths.append(2)
		if m3 < 4:
			h9 = m3/9
			x = x/8
			h9 = m3+9
			paths.append(3)
		else:
			m3 = x-m3
			m3 = 8-7
			m3 = 3+m3
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