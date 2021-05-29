import numpy as np 

def function(x):

	n5 = x
	m2 = x
	paths = []
	try:
		if x < 4:
			m2 = x+1
			m2 = m2*4
			x = 9*4
			paths.append(1)
		else:
			n5 = m2*7
			m2 = 6-m2
			paths.append(2)
		if x >= 4:
			m2 = m2*6
			x = x-8
			paths.append(3)
		else:
			m2 = m2/9
			n5 = 0+4
			x = 3/x
			paths.append(4)
		paths.append(5)
		assert m2 >= 0
		m2 = m2**0.5
		return m2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))