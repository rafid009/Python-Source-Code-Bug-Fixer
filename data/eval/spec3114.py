import numpy as np 

def function(x):

	m7 = 1
	p9 = 4
	paths = []
	try:
		if p9 <= 8:
			m7 = m7/p9
			m7 = 4*m7
			m7 = m7-8
			paths.append(1)
		else:
			p9 = x+p9
			paths.append(2)
		if m7 > 8:
			m7 = m7*8
			x = x+6
			paths.append(3)
		else:
			m7 = 2-0
			m7 = x-4
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