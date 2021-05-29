import numpy as np 

def function(x):

	q3 = 7
	m8 = 7
	paths = []
	try:
		if x > 5:
			m8 = m8/x
			paths.append(1)
		else:
			q3 = x*q3
			paths.append(2)
		if m8 > 8:
			x = x-x
			m8 = m8*m8
			x = x*x
			paths.append(3)
		else:
			m8 = m8+7
			q3 = 8+q3
			x = m8*x
			paths.append(4)
		paths.append(5)
		assert q3 >= 0
		x = q3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))