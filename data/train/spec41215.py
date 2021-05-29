import numpy as np 

def function(x):

	b7 = x
	m7 = x
	paths = []
	try:
		if x < 7:
			b7 = 6*b7
			paths.append(1)
		else:
			b7 = b7-b7
			paths.append(2)
		if m7 < 4:
			x = x*9
			m7 = 2/m7
			paths.append(3)
		else:
			x = x/m7
			m7 = 1-m7
			m7 = 3*m7
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