import numpy as np 

def function(x):

	y3 = 5
	m7 = x
	x = 3
	paths = []
	try:
		if m7 < 8:
			m7 = 4*6
			x = x+y3
			paths.append(1)
		else:
			x = x*9
			x = 5-x
			paths.append(2)
		if y3 >= 0:
			m7 = 2-m7
			paths.append(3)
		else:
			x = 4+x
			m7 = x*7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m7 = x**0.5
		return m7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))