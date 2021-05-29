import numpy as np 

def function(x):

	b3 = 2
	m0 = 3
	paths = []
	try:
		if b3 <= 0:
			m0 = 5/b3
			paths.append(1)
		else:
			m0 = 6/6
			x = x*9
			b3 = m0+b3
			paths.append(2)
		if b3 < 3:
			x = m0/m0
			x = 0+0
			paths.append(3)
		else:
			m0 = b3-x
			m0 = m0+m0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b3 = x**0.5
		return b3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))