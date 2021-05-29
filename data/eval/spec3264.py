import numpy as np 

def function(x):

	m7 = x
	b7 = 4
	paths = []
	try:
		if m7 > 1:
			b7 = b7*8
			paths.append(1)
		else:
			m7 = 7/m7
			m7 = b7/6
			paths.append(2)
		if x < 0:
			b7 = x/7
			paths.append(3)
		else:
			m7 = m7+m7
			x = b7/3
			b7 = 2-b7
			paths.append(4)
		paths.append(5)
		assert b7 >= 0
		b7 = b7**0.5
		return b7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))