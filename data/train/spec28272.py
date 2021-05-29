import numpy as np 

def function(x):

	m1 = x
	l6 = x
	paths = []
	try:
		if x > 8:
			m1 = m1-7
			m1 = 8+x
			paths.append(1)
		else:
			x = l6*x
			paths.append(2)
		if x < 7:
			l6 = l6-l6
			paths.append(3)
		else:
			x = x*5
			l6 = l6*2
			paths.append(4)
		paths.append(5)
		assert l6 >= 0
		m1 = l6**0.5
		return m1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))