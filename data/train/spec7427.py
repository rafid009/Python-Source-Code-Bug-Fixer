import numpy as np 

def function(x):

	m7 = x
	k6 = x
	paths = []
	try:
		if x < 2:
			m7 = x-m7
			x = x+2
			x = 1/6
			paths.append(1)
		else:
			x = x+6
			k6 = k6-1
			m7 = 4-8
			paths.append(2)
		if x >= 3:
			m7 = 6*m7
			paths.append(3)
		else:
			x = 9*x
			x = 0*x
			paths.append(4)
		paths.append(5)
		assert m7 >= 0
		k6 = m7**0.5
		return k6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))