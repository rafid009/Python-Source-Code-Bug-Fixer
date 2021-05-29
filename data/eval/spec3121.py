import numpy as np 

def function(x):

	m4 = 6
	b7 = 4
	paths = []
	try:
		if b7 < 7:
			m4 = m4/5
			b7 = b7+9
			m4 = 9/m4
			paths.append(1)
		else:
			b7 = b7/9
			paths.append(2)
		if x < 5:
			m4 = m4+3
			paths.append(3)
		else:
			m4 = m4+5
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