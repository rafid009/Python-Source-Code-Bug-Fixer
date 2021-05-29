import numpy as np 

def function(x):

	m2 = x
	h0 = x
	paths = []
	try:
		if h0 < 4:
			x = x*1
			m2 = m2-8
			m2 = 6/x
			paths.append(1)
		else:
			h0 = 1+0
			m2 = 5*m2
			paths.append(2)
		if x <= 0:
			m2 = 3*9
			x = x+x
			x = h0+2
			paths.append(3)
		else:
			m2 = 5/m2
			paths.append(4)
		paths.append(5)
		assert h0 >= 0
		m2 = h0**0.5
		return m2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))