import numpy as np 

def function(x):

	m9 = x
	b2 = x
	x = 0
	paths = []
	try:
		if m9 < 5:
			b2 = b2+7
			x = x-4
			m9 = m9*m9
			paths.append(1)
		else:
			m9 = 2/8
			paths.append(2)
		if b2 <= 6:
			b2 = 7/b2
			paths.append(3)
		else:
			x = 2*7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b2 = x**0.5
		return b2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))