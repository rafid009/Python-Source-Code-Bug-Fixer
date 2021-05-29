import numpy as np 

def function(x):

	b4 = x
	m4 = 7
	x = x
	paths = []
	try:
		if b4 > 2:
			x = x-x
			paths.append(1)
		else:
			m4 = 6-m4
			m4 = 3+x
			b4 = 0+b4
			paths.append(2)
		if x < 4:
			b4 = b4/2
			m4 = 6*m4
			m4 = m4-x
			paths.append(3)
		else:
			m4 = m4/2
			m4 = b4+0
			paths.append(4)
		paths.append(5)
		assert m4 >= 0
		x = m4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))