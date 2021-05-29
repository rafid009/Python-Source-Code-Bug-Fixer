import numpy as np 

def function(x):

	b7 = 9
	m3 = x
	paths = []
	try:
		if m3 > 1:
			b7 = 0*b7
			x = x+7
			paths.append(1)
		else:
			m3 = m3/1
			paths.append(2)
		if x <= 2:
			m3 = b7-m3
			paths.append(3)
		else:
			b7 = m3+b7
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