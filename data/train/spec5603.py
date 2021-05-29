import numpy as np 

def function(x):

	m3 = 1
	b8 = 3
	paths = []
	try:
		if b8 < 4:
			b8 = 1-b8
			b8 = b8*2
			paths.append(1)
		else:
			b8 = 6-0
			m3 = 8-m3
			paths.append(2)
		if b8 < 3:
			m3 = m3/4
			b8 = b8+b8
			paths.append(3)
		else:
			m3 = 0/m3
			b8 = 6/b8
			paths.append(4)
		paths.append(5)
		assert b8 >= 0
		m3 = b8**0.5
		return m3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))