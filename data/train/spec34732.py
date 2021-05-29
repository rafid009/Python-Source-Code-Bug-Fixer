import numpy as np 

def function(x):

	m2 = 7
	l6 = 0
	paths = []
	try:
		if m2 > 9:
			x = 2+x
			paths.append(1)
		else:
			l6 = m2+m2
			x = x/7
			paths.append(2)
		if x > 0:
			m2 = m2*8
			m2 = l6+m2
			m2 = m2+l6
			paths.append(3)
		else:
			l6 = 4-l6
			paths.append(4)
		paths.append(5)
		assert l6 >= 0
		x = l6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))