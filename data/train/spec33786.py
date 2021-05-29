import numpy as np 

def function(x):

	m7 = x
	b2 = 3
	paths = []
	try:
		if b2 < 4:
			m7 = 3+m7
			paths.append(1)
		else:
			m7 = m7/5
			m7 = x/3
			paths.append(2)
		if m7 > 6:
			x = 7-x
			paths.append(3)
		else:
			x = 5*7
			b2 = m7+b2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))