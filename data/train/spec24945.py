import numpy as np 

def function(x):

	b6 = 9
	m7 = 2
	paths = []
	try:
		if m7 > 9:
			b6 = 7*m7
			b6 = b6/m7
			m7 = 6*m7
			paths.append(1)
		else:
			m7 = m7/7
			paths.append(2)
		if b6 > 9:
			b6 = b6+4
			x = x-6
			paths.append(3)
		else:
			x = 8/x
			m7 = m7-7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b6 = x**0.5
		return b6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))