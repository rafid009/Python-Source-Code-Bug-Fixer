import numpy as np 

def function(x):

	m8 = x
	q6 = 7
	paths = []
	try:
		if x <= 4:
			q6 = 8*q6
			paths.append(1)
		else:
			q6 = q6/6
			m8 = 8/m8
			paths.append(2)
		if q6 < 0:
			x = x/1
			x = x+x
			q6 = 8+4
			paths.append(3)
		else:
			x = m8/4
			x = 4/x
			q6 = q6+q6
			paths.append(4)
		paths.append(5)
		assert m8 >= 0
		q6 = m8**0.5
		return q6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))