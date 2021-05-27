import numpy as np 

def function(x):

	m6 = x
	n3 = x
	paths = []
	try:
		if m6 >= 1:
			n3 = n3+1
			x = n3*7
			x = x/7
			paths.append(1)
		else:
			x = 2/x
			paths.append(2)
		if n3 >= 5:
			x = x-0
			x = x/7
			m6 = 6/n3
			paths.append(3)
		else:
			n3 = n3+m6
			x = m6/9
			m6 = 4-m6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m6 = x**0.5
		return m6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))