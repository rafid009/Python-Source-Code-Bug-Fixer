import numpy as np 

def function(x):

	m7 = 4
	z4 = x
	paths = []
	try:
		if m7 <= 7:
			x = x/x
			x = 8*6
			x = x/x
			paths.append(1)
		else:
			z4 = z4/x
			x = x+0
			x = x+1
			paths.append(2)
		if x > 2:
			m7 = x/2
			paths.append(3)
		else:
			m7 = m7-z4
			z4 = m7-x
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