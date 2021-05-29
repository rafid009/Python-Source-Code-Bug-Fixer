import numpy as np 

def function(x):

	j5 = x
	m2 = 9
	paths = []
	try:
		if j5 < 1:
			x = 1+x
			m2 = 3*3
			j5 = j5/3
			paths.append(1)
		else:
			m2 = m2*j5
			x = x-j5
			paths.append(2)
		if j5 <= 1:
			j5 = 5-x
			paths.append(3)
		else:
			x = x/7
			x = x-7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m2 = x**0.5
		return m2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))