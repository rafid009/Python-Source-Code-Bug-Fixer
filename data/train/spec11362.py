import numpy as np 

def function(x):

	m7 = x
	r9 = x
	x = 5
	paths = []
	try:
		if x <= 6:
			x = x/x
			paths.append(1)
		else:
			x = 9+m7
			paths.append(2)
		if r9 > 5:
			x = 9/x
			paths.append(3)
		else:
			x = r9*8
			m7 = m7/2
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