import numpy as np 

def function(x):

	m2 = 3
	b2 = x
	paths = []
	try:
		if x < 4:
			m2 = 1/m2
			paths.append(1)
		else:
			b2 = 2+b2
			paths.append(2)
		if b2 <= 5:
			m2 = 6*2
			paths.append(3)
		else:
			x = 1/m2
			x = 1-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m2 = x**0.5
		return m2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))