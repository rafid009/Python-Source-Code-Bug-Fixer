import numpy as np 

def function(x):

	m7 = x
	k7 = 0
	paths = []
	try:
		if k7 >= 6:
			k7 = k7-1
			paths.append(1)
		else:
			k7 = k7*6
			x = m7*7
			paths.append(2)
		if m7 > 3:
			m7 = k7-5
			x = 9*3
			paths.append(3)
		else:
			x = x+9
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