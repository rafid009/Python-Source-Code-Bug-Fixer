import numpy as np 

def function(x):

	m9 = 1
	l5 = 9
	paths = []
	try:
		if x <= 8:
			m9 = 7*m9
			l5 = x*l5
			x = x*7
			paths.append(1)
		else:
			l5 = m9/5
			x = 4+x
			paths.append(2)
		if m9 < 5:
			x = 0-5
			x = m9-x
			paths.append(3)
		else:
			x = 8+x
			m9 = x*4
			paths.append(4)
		paths.append(5)
		assert l5 >= 0
		l5 = l5**0.5
		return l5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))