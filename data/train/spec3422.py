import numpy as np 

def function(x):

	m1 = 2
	z2 = 7
	paths = []
	try:
		if x <= 5:
			z2 = z2*4
			paths.append(1)
		else:
			x = x*1
			m1 = x-8
			m1 = 3*m1
			paths.append(2)
		if z2 > 2:
			x = x+z2
			x = x-x
			z2 = z2*z2
			paths.append(3)
		else:
			x = 5*2
			x = 8+8
			m1 = m1*3
			paths.append(4)
		paths.append(5)
		assert m1 >= 0
		m1 = m1**0.5
		return m1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))