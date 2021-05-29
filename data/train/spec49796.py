import numpy as np 

def function(x):

	m3 = 8
	e3 = 8
	paths = []
	try:
		if x >= 5:
			e3 = 7*8
			paths.append(1)
		else:
			m3 = e3+e3
			paths.append(2)
		if x >= 9:
			e3 = 9+2
			m3 = 7/m3
			paths.append(3)
		else:
			m3 = x/6
			m3 = m3/7
			x = x+5
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