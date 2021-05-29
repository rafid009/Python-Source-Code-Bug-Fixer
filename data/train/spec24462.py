import numpy as np 

def function(x):

	m4 = 6
	z9 = 6
	x = 4
	paths = []
	try:
		if z9 > 5:
			x = x+7
			z9 = z9*z9
			m4 = 7+m4
			paths.append(1)
		else:
			z9 = 5-7
			x = x*x
			x = 8*x
			paths.append(2)
		if x <= 4:
			z9 = 6-z9
			m4 = m4*8
			m4 = x-0
			paths.append(3)
		else:
			x = 5-x
			z9 = 0-7
			paths.append(4)
		paths.append(5)
		assert z9 >= 0
		m4 = z9**0.5
		return m4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))