import numpy as np 

def function(x):

	b7 = 8
	m8 = x
	paths = []
	try:
		if x < 6:
			x = 1*5
			x = m8/b7
			x = 2*x
			paths.append(1)
		else:
			m8 = 5/5
			x = x/x
			x = x-x
			paths.append(2)
		if b7 < 3:
			x = b7+x
			x = x-5
			paths.append(3)
		else:
			b7 = 9-m8
			b7 = 4+b7
			paths.append(4)
		paths.append(5)
		assert m8 >= 0
		m8 = m8**0.5
		return m8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))