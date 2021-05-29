import numpy as np 

def function(x):

	z1 = x
	m7 = 2
	paths = []
	try:
		if m7 >= 9:
			z1 = z1*0
			paths.append(1)
		else:
			m7 = 1+8
			z1 = z1/3
			x = 0+x
			paths.append(2)
		if z1 > 4:
			m7 = x/x
			paths.append(3)
		else:
			m7 = m7+3
			paths.append(4)
		paths.append(5)
		assert z1 >= 0
		z1 = z1**0.5
		return z1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))