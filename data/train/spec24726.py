import numpy as np 

def function(x):

	j3 = x
	m6 = x
	x = 5
	paths = []
	try:
		if m6 >= 9:
			j3 = 7+j3
			m6 = 0*j3
			paths.append(1)
		else:
			j3 = j3/2
			paths.append(2)
		if x >= 6:
			j3 = m6-j3
			j3 = 6-6
			paths.append(3)
		else:
			j3 = j3/7
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