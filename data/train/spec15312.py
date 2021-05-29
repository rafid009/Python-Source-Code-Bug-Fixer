import numpy as np 

def function(x):

	m3 = 2
	t2 = 0
	paths = []
	try:
		if m3 >= 4:
			m3 = m3/2
			paths.append(1)
		else:
			t2 = t2*t2
			x = 8/x
			m3 = m3+2
			paths.append(2)
		if m3 < 3:
			x = 9+6
			paths.append(3)
		else:
			x = 6*x
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