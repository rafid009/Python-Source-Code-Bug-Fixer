import numpy as np 

def function(x):

	m3 = x
	b3 = 7
	paths = []
	try:
		if m3 < 8:
			b3 = b3-b3
			x = x+3
			paths.append(1)
		else:
			m3 = m3-1
			m3 = 8/m3
			paths.append(2)
		if b3 >= 7:
			m3 = 7*b3
			paths.append(3)
		else:
			b3 = x+m3
			x = 1+x
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