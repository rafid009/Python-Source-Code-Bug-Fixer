import numpy as np 

def function(x):

	m9 = x
	l9 = 2
	x = 6
	paths = []
	try:
		if x > 7:
			x = x+l9
			paths.append(1)
		else:
			x = x-8
			paths.append(2)
		if x <= 9:
			l9 = l9*m9
			x = x*x
			paths.append(3)
		else:
			m9 = 7-6
			l9 = 1*l9
			m9 = m9-0
			paths.append(4)
		paths.append(5)
		assert l9 >= 0
		x = l9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))