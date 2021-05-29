import numpy as np 

def function(x):

	x9 = 4
	m6 = 9
	x = 8
	paths = []
	try:
		if x < 8:
			m6 = 8-9
			paths.append(1)
		else:
			x9 = x9*7
			x9 = m6-x9
			m6 = m6+x
			paths.append(2)
		if x < 7:
			m6 = x9*m6
			m6 = m6+2
			x = x/7
			paths.append(3)
		else:
			m6 = 5+x
			x = 7+x
			m6 = x*3
			paths.append(4)
		paths.append(5)
		assert x9 >= 0
		x = x9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))