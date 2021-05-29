import numpy as np 

def function(x):

	m8 = 1
	l7 = x
	paths = []
	try:
		if m8 > 5:
			l7 = 6/4
			m8 = m8-0
			paths.append(1)
		else:
			l7 = l7*4
			m8 = 7*m8
			x = x/2
			paths.append(2)
		if l7 > 9:
			m8 = 0/m8
			paths.append(3)
		else:
			m8 = m8-m8
			x = x/l7
			x = 5/l7
			paths.append(4)
		paths.append(5)
		assert l7 >= 0
		x = l7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))