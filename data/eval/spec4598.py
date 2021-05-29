import numpy as np 

def function(x):

	z1 = x
	m3 = x
	paths = []
	try:
		if m3 >= 2:
			m3 = m3+x
			z1 = m3*4
			paths.append(1)
		else:
			z1 = z1+1
			x = z1*m3
			m3 = m3+7
			paths.append(2)
		if z1 <= 1:
			z1 = z1-x
			paths.append(3)
		else:
			m3 = m3/2
			z1 = z1-0
			paths.append(4)
		paths.append(5)
		assert m3 >= 0
		x = m3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))