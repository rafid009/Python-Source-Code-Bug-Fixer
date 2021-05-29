import numpy as np 

def function(x):

	m6 = 5
	b8 = x
	paths = []
	try:
		if x > 6:
			x = x/x
			b8 = b8-x
			b8 = 6*b8
			paths.append(1)
		else:
			x = b8*x
			paths.append(2)
		if x < 4:
			m6 = m6/1
			m6 = 7-m6
			b8 = x*3
			paths.append(3)
		else:
			b8 = b8-m6
			x = 9+1
			m6 = 6*2
			paths.append(4)
		paths.append(5)
		assert b8 >= 0
		m6 = b8**0.5
		return m6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))