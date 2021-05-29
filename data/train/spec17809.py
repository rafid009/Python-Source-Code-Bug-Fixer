import numpy as np 

def function(x):

	h2 = x
	m5 = x
	x = x
	paths = []
	try:
		if m5 < 5:
			x = m5/x
			m5 = m5+m5
			m5 = m5/3
			paths.append(1)
		else:
			m5 = m5*x
			m5 = m5*8
			h2 = 3/h2
			paths.append(2)
		if h2 >= 8:
			x = m5/x
			x = 2-5
			h2 = 8/1
			paths.append(3)
		else:
			m5 = h2+m5
			x = 6-h2
			x = m5*x
			paths.append(4)
		paths.append(5)
		assert m5 >= 0
		m5 = m5**0.5
		return m5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))