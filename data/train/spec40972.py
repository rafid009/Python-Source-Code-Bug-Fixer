import numpy as np 

def function(x):

	j3 = 3
	m6 = 4
	paths = []
	try:
		if m6 > 5:
			m6 = m6*m6
			m6 = m6+m6
			x = x-x
			paths.append(1)
		else:
			x = m6*m6
			j3 = 6/j3
			paths.append(2)
		if m6 <= 8:
			m6 = 6-8
			paths.append(3)
		else:
			x = x+x
			x = x+8
			paths.append(4)
		paths.append(5)
		assert m6 >= 0
		x = m6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))