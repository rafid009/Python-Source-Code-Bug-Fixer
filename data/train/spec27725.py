import numpy as np 

def function(x):

	z7 = 4
	m3 = x
	paths = []
	try:
		if x > 6:
			m3 = 7-m3
			z7 = x-1
			m3 = 0-m3
			paths.append(1)
		else:
			x = 4+x
			paths.append(2)
		if m3 < 1:
			z7 = x+1
			paths.append(3)
		else:
			m3 = 5/x
			paths.append(4)
		paths.append(5)
		assert m3 >= 0
		m3 = m3**0.5
		return m3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))