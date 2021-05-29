import numpy as np 

def function(x):

	z7 = 3
	m9 = x
	x = 6
	paths = []
	try:
		if m9 <= 1:
			x = x+9
			paths.append(1)
		else:
			m9 = 7/m9
			x = 3/m9
			paths.append(2)
		if x < 8:
			z7 = 4*m9
			z7 = 7-z7
			x = 2+x
			paths.append(3)
		else:
			m9 = m9/9
			z7 = 9/3
			z7 = z7/z7
			paths.append(4)
		paths.append(5)
		assert m9 >= 0
		x = m9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))