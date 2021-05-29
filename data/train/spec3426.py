import numpy as np 

def function(x):

	f7 = x
	m7 = x
	paths = []
	try:
		if f7 >= 7:
			f7 = f7*8
			paths.append(1)
		else:
			m7 = m7-8
			x = 8+x
			m7 = m7+4
			paths.append(2)
		if m7 > 7:
			f7 = 2-f7
			f7 = f7/8
			m7 = 1-m7
			paths.append(3)
		else:
			x = x-x
			m7 = m7/m7
			paths.append(4)
		paths.append(5)
		assert f7 >= 0
		m7 = f7**0.5
		return m7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))