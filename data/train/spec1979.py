import numpy as np 

def function(x):

	w9 = x
	m7 = 3
	paths = []
	try:
		if x < 6:
			m7 = 2-9
			paths.append(1)
		else:
			x = 5-w9
			x = x/8
			m7 = m7/x
			paths.append(2)
		if m7 < 2:
			m7 = 5-w9
			paths.append(3)
		else:
			x = 2-x
			paths.append(4)
		paths.append(5)
		assert m7 >= 0
		w9 = m7**0.5
		return w9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))