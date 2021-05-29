import numpy as np 

def function(x):

	m2 = x
	y3 = x
	paths = []
	try:
		if x >= 0:
			x = m2+y3
			y3 = 9+2
			paths.append(1)
		else:
			y3 = y3/9
			m2 = 0*m2
			m2 = m2+0
			paths.append(2)
		if m2 <= 8:
			m2 = 7*m2
			m2 = x+9
			y3 = y3/x
			paths.append(3)
		else:
			m2 = m2/9
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