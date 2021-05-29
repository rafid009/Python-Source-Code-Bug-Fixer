import numpy as np 

def function(x):

	m6 = x
	n5 = 1
	paths = []
	try:
		if x <= 6:
			n5 = 3-n5
			m6 = 5+m6
			paths.append(1)
		else:
			x = 5/n5
			x = x/x
			paths.append(2)
		if n5 > 4:
			x = 7/x
			x = x/2
			paths.append(3)
		else:
			x = x*9
			x = 5-x
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