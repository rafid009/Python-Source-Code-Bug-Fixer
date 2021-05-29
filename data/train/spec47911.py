import numpy as np 

def function(x):

	r6 = 4
	m6 = x
	paths = []
	try:
		if x <= 5:
			x = 2-x
			x = m6/x
			paths.append(1)
		else:
			r6 = r6/7
			x = 6+m6
			paths.append(2)
		if x >= 8:
			r6 = x/r6
			r6 = x/1
			x = x-6
			paths.append(3)
		else:
			m6 = 1+m6
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