import numpy as np 

def function(x):

	l8 = x
	m7 = 0
	x = x
	paths = []
	try:
		if l8 < 1:
			x = x*x
			m7 = m7-6
			paths.append(1)
		else:
			l8 = x/6
			paths.append(2)
		if m7 <= 5:
			m7 = l8*1
			x = 9+3
			paths.append(3)
		else:
			x = 6-x
			paths.append(4)
		paths.append(5)
		assert m7 >= 0
		x = m7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))