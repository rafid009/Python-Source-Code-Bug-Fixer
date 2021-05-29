import numpy as np 

def function(x):

	m1 = x
	z7 = x
	x = 6
	paths = []
	try:
		if m1 < 7:
			m1 = 9+m1
			x = x+x
			m1 = 1+4
			paths.append(1)
		else:
			z7 = z7*5
			z7 = 7/5
			z7 = z7-7
			paths.append(2)
		if z7 <= 5:
			x = z7/8
			z7 = z7+4
			m1 = x-2
			paths.append(3)
		else:
			m1 = 1/m1
			m1 = m1-7
			paths.append(4)
		paths.append(5)
		assert z7 >= 0
		m1 = z7**0.5
		return m1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))