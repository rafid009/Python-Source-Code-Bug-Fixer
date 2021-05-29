import numpy as np 

def function(x):

	m3 = x
	b7 = x
	paths = []
	try:
		if b7 > 5:
			m3 = m3+6
			m3 = m3/6
			b7 = m3-b7
			paths.append(1)
		else:
			x = m3-x
			x = x-4
			b7 = 0+b7
			paths.append(2)
		if b7 >= 8:
			b7 = 2+8
			x = 9-x
			paths.append(3)
		else:
			b7 = b7*x
			paths.append(4)
		paths.append(5)
		assert m3 >= 0
		m3 = m3**0.5
		return m3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))