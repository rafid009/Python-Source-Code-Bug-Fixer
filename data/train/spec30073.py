import numpy as np 

def function(x):

	m4 = 4
	n8 = 9
	paths = []
	try:
		if n8 < 2:
			m4 = m4-n8
			x = x/1
			paths.append(1)
		else:
			n8 = n8-4
			n8 = 7*n8
			m4 = x*m4
			paths.append(2)
		if m4 > 8:
			m4 = m4+5
			paths.append(3)
		else:
			n8 = 8*4
			n8 = n8/5
			n8 = n8-1
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