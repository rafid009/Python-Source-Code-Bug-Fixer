import numpy as np 

def function(x):

	f0 = 1
	m7 = x
	paths = []
	try:
		if f0 <= 3:
			x = 5*m7
			paths.append(1)
		else:
			m7 = m7*4
			paths.append(2)
		if m7 >= 5:
			f0 = f0*f0
			m7 = x*m7
			paths.append(3)
		else:
			f0 = 5/2
			m7 = m7*7
			paths.append(4)
		paths.append(5)
		assert m7 >= 0
		m7 = m7**0.5
		return m7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))