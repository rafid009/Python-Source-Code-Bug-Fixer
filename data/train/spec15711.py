import numpy as np 

def function(x):

	q6 = x
	m7 = x
	paths = []
	try:
		if q6 > 7:
			m7 = q6+4
			q6 = q6-7
			m7 = 2/m7
			paths.append(1)
		else:
			x = m7/x
			paths.append(2)
		if x >= 2:
			q6 = 6*1
			m7 = 6-5
			paths.append(3)
		else:
			m7 = 8/m7
			paths.append(4)
		paths.append(5)
		assert q6 >= 0
		x = q6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))