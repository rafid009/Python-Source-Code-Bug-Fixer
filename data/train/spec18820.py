import numpy as np 

def function(x):

	m7 = x
	n3 = x
	x = 8
	paths = []
	try:
		if m7 <= 9:
			m7 = m7*5
			n3 = 9/n3
			paths.append(1)
		else:
			x = 4/n3
			n3 = 0/9
			paths.append(2)
		if n3 <= 8:
			m7 = m7+6
			paths.append(3)
		else:
			x = 8-x
			m7 = m7/n3
			paths.append(4)
		paths.append(5)
		assert n3 >= 0
		m7 = n3**0.5
		return m7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))