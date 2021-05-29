import numpy as np 

def function(x):

	h0 = 5
	m7 = 4
	paths = []
	try:
		if x < 1:
			m7 = x/3
			paths.append(1)
		else:
			h0 = h0+h0
			m7 = 0-x
			m7 = m7*9
			paths.append(2)
		if m7 >= 8:
			x = x*h0
			m7 = 3-1
			paths.append(3)
		else:
			m7 = x/5
			m7 = x+9
			h0 = 5-m7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m7 = x**0.5
		return m7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))