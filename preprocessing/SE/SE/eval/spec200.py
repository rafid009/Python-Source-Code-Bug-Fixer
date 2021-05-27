import numpy as np 

def function(x):

	l5 = x
	m5 = x
	paths = []
	try:
		if x < 8:
			m5 = m5+m5
			paths.append(1)
		else:
			x = 0*l5
			paths.append(2)
		if m5 <= 4:
			m5 = x/9
			m5 = 9*6
			l5 = l5*l5
			paths.append(3)
		else:
			m5 = x-m5
			l5 = 8*l5
			x = l5/3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l5 = x**0.5
		return l5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))