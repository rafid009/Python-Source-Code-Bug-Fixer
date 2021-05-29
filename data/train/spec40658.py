import numpy as np 

def function(x):

	q9 = 6
	m7 = 1
	paths = []
	try:
		if m7 > 4:
			q9 = x/6
			paths.append(1)
		else:
			m7 = 5-q9
			paths.append(2)
		if x < 2:
			m7 = 9-m7
			paths.append(3)
		else:
			m7 = 3-m7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m7 = x**0.5
		return m7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))