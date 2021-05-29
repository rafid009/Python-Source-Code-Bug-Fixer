import numpy as np 

def function(x):

	m7 = 6
	x4 = 2
	x = x
	paths = []
	try:
		if x4 <= 3:
			m7 = 2+9
			paths.append(1)
		else:
			m7 = 0-m7
			x = m7/9
			x = x-1
			paths.append(2)
		if x4 < 4:
			x4 = 1/2
			m7 = 6/m7
			x4 = 5-m7
			paths.append(3)
		else:
			m7 = m7*7
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