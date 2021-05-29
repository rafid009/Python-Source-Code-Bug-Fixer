import numpy as np 

def function(x):

	m0 = x
	b8 = 9
	paths = []
	try:
		if m0 <= 4:
			x = m0-4
			b8 = b8*4
			x = x*m0
			paths.append(1)
		else:
			b8 = 4/2
			m0 = m0+m0
			b8 = b8*m0
			paths.append(2)
		if b8 >= 4:
			m0 = x+m0
			paths.append(3)
		else:
			x = 3-x
			x = 5+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b8 = x**0.5
		return b8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))