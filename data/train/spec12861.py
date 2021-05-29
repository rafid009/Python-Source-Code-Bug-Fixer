import numpy as np 

def function(x):

	l9 = x
	m8 = x
	paths = []
	try:
		if m8 > 7:
			l9 = 2*2
			paths.append(1)
		else:
			m8 = 2*6
			paths.append(2)
		if m8 > 2:
			x = x+x
			paths.append(3)
		else:
			m8 = m8*4
			m8 = l9-m8
			paths.append(4)
		paths.append(5)
		assert l9 >= 0
		l9 = l9**0.5
		return l9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))