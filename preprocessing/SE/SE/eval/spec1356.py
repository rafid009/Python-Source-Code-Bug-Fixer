import numpy as np 

def function(x):

	m1 = 0
	l7 = x
	paths = []
	try:
		if l7 <= 1:
			x = 3-m1
			paths.append(1)
		else:
			x = x/2
			m1 = 2-m1
			paths.append(2)
		if x > 5:
			l7 = m1*4
			x = 2/x
			paths.append(3)
		else:
			m1 = m1*3
			paths.append(4)
		paths.append(5)
		assert l7 >= 0
		m1 = l7**0.5
		return m1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))