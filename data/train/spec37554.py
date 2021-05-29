import numpy as np 

def function(x):

	m5 = 1
	z5 = x
	paths = []
	try:
		if m5 <= 3:
			z5 = z5*5
			m5 = 7/1
			paths.append(1)
		else:
			m5 = m5*3
			x = x*x
			m5 = m5+z5
			paths.append(2)
		if x <= 5:
			m5 = 4/7
			z5 = z5/9
			paths.append(3)
		else:
			x = 8/z5
			m5 = m5/z5
			z5 = z5+0
			paths.append(4)
		paths.append(5)
		assert z5 >= 0
		m5 = z5**0.5
		return m5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))