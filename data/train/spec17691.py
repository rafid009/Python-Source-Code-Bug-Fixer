import numpy as np 

def function(x):

	m7 = x
	a3 = x
	paths = []
	try:
		if m7 < 2:
			m7 = m7-2
			paths.append(1)
		else:
			m7 = m7-m7
			x = 9*m7
			x = 9+0
			paths.append(2)
		if a3 > 3:
			a3 = m7-5
			m7 = 4*m7
			paths.append(3)
		else:
			x = 3/a3
			x = a3-a3
			paths.append(4)
		paths.append(5)
		assert a3 >= 0
		x = a3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))