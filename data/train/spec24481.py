import numpy as np 

def function(x):

	m3 = x
	paths = []
	try:
		if m3 < 0:
			m3 = 7-6
			paths.append(1)
		else:
			x = 1-x
			paths.append(2)
		if m3 < 4:
			m3 = x/m3
			m3 = x-m3
			paths.append(3)
		else:
			m3 = 9+m3
			m3 = 9+m3
			x = 2-2
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