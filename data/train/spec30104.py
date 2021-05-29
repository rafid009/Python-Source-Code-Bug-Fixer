import numpy as np 

def function(x):

	j6 = 8
	m8 = x
	paths = []
	try:
		if j6 > 1:
			m8 = 7-m8
			paths.append(1)
		else:
			m8 = 3+7
			m8 = 9*x
			m8 = 2-m8
			paths.append(2)
		if m8 >= 4:
			j6 = j6/8
			m8 = 9*m8
			j6 = j6-m8
			paths.append(3)
		else:
			j6 = 3-j6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m8 = x**0.5
		return m8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))