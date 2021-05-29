import numpy as np 

def function(x):

	m7 = 9
	l0 = 0
	x = x
	paths = []
	try:
		if m7 <= 5:
			m7 = l0/9
			m7 = m7-9
			x = 0+2
			paths.append(1)
		else:
			m7 = m7*9
			m7 = l0+l0
			m7 = l0*7
			paths.append(2)
		if x < 0:
			l0 = 1-9
			paths.append(3)
		else:
			l0 = l0*7
			m7 = 3/4
			paths.append(4)
		paths.append(5)
		assert l0 >= 0
		x = l0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))