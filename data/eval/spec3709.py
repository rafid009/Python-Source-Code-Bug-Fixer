import numpy as np 

def function(x):

	m3 = 1
	h0 = 0
	paths = []
	try:
		if m3 < 5:
			x = 6/x
			m3 = 2-8
			paths.append(1)
		else:
			x = 0/1
			m3 = m3*4
			x = x*4
			paths.append(2)
		if x > 8:
			h0 = x/4
			m3 = h0/7
			paths.append(3)
		else:
			h0 = m3*0
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