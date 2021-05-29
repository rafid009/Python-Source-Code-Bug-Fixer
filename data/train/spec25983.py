import numpy as np 

def function(x):

	n6 = 9
	m6 = x
	paths = []
	try:
		if n6 <= 3:
			m6 = 9/4
			x = 3+x
			n6 = 7+n6
			paths.append(1)
		else:
			x = x+x
			paths.append(2)
		if m6 <= 8:
			n6 = n6*0
			paths.append(3)
		else:
			n6 = x*x
			x = x-x
			paths.append(4)
		paths.append(5)
		assert m6 >= 0
		m6 = m6**0.5
		return m6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))