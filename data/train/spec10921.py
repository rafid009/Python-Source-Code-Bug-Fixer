import numpy as np 

def function(x):

	m7 = x
	a1 = 5
	paths = []
	try:
		if m7 > 2:
			m7 = a1-m7
			m7 = 5/m7
			paths.append(1)
		else:
			a1 = 6/x
			m7 = m7+x
			a1 = a1*7
			paths.append(2)
		if m7 <= 2:
			x = x-m7
			a1 = 7-0
			paths.append(3)
		else:
			m7 = m7/m7
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