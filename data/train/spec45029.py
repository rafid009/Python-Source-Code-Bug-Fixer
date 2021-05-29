import numpy as np 

def function(x):

	x7 = 9
	m8 = x
	paths = []
	try:
		if x7 <= 7:
			x7 = x7-2
			m8 = m8+8
			x = x+x
			paths.append(1)
		else:
			x7 = 3*7
			x = x*6
			paths.append(2)
		if m8 <= 4:
			x7 = 6/m8
			m8 = m8*x7
			x = x+m8
			paths.append(3)
		else:
			x = x/x
			m8 = m8*5
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