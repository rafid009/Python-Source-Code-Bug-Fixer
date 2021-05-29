import numpy as np 

def function(x):

	m3 = 3
	m7 = 0
	paths = []
	try:
		if x <= 4:
			m3 = m3+1
			paths.append(1)
		else:
			m7 = 3*m7
			x = x*8
			paths.append(2)
		if x <= 6:
			m7 = 0-x
			paths.append(3)
		else:
			m3 = m3*3
			x = x*2
			m3 = 8+m3
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