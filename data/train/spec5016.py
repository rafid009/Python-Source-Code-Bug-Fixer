import numpy as np 

def function(x):

	t0 = 5
	m4 = 3
	paths = []
	try:
		if m4 > 5:
			m4 = 6-m4
			m4 = 3/m4
			t0 = 7*5
			paths.append(1)
		else:
			t0 = 8/t0
			paths.append(2)
		if m4 <= 8:
			x = 7/x
			m4 = 3-m4
			paths.append(3)
		else:
			x = 8*8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m4 = x**0.5
		return m4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))