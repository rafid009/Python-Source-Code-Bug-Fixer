import numpy as np 

def function(x):

	l1 = 1
	m2 = 9
	paths = []
	try:
		if l1 > 9:
			m2 = 0+m2
			x = 9+x
			paths.append(1)
		else:
			l1 = 2+x
			x = 6-8
			paths.append(2)
		if l1 > 3:
			m2 = m2+1
			x = l1*6
			m2 = m2+8
			paths.append(3)
		else:
			m2 = m2*m2
			m2 = 4*m2
			paths.append(4)
		paths.append(5)
		assert l1 >= 0
		m2 = l1**0.5
		return m2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))