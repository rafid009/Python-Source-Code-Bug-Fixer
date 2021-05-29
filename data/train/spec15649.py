import numpy as np 

def function(x):

	m7 = 9
	k2 = 4
	paths = []
	try:
		if k2 < 7:
			m7 = m7+8
			k2 = k2+x
			paths.append(1)
		else:
			m7 = 7+k2
			m7 = 9+4
			paths.append(2)
		if k2 > 0:
			m7 = m7/2
			x = 2*x
			x = x+1
			paths.append(3)
		else:
			x = 5-m7
			m7 = m7/m7
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