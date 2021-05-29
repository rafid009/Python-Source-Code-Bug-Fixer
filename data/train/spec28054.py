import numpy as np 

def function(x):

	p6 = x
	m7 = 6
	paths = []
	try:
		if p6 <= 9:
			x = 4+x
			m7 = p6+5
			paths.append(1)
		else:
			m7 = m7+4
			m7 = m7-p6
			paths.append(2)
		if m7 < 4:
			m7 = 6/p6
			p6 = m7/2
			p6 = 2+3
			paths.append(3)
		else:
			p6 = 1/p6
			m7 = 9+m7
			m7 = m7*m7
			paths.append(4)
		paths.append(5)
		assert m7 >= 0
		x = m7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))