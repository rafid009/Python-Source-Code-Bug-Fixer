import numpy as np 

def function(x):

	m8 = 4
	z2 = 7
	x = x
	paths = []
	try:
		if m8 > 8:
			x = 5/5
			x = x+3
			m8 = 5*8
			paths.append(1)
		else:
			m8 = m8-m8
			m8 = x-8
			x = 8+x
			paths.append(2)
		if z2 > 9:
			x = x/9
			x = x*6
			z2 = 5+z2
			paths.append(3)
		else:
			x = 0*x
			paths.append(4)
		paths.append(5)
		assert m8 >= 0
		x = m8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))