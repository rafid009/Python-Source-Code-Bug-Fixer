import numpy as np 

def function(x):

	q9 = 2
	m9 = x
	paths = []
	try:
		if q9 >= 2:
			x = 5/q9
			q9 = 1/q9
			paths.append(1)
		else:
			q9 = m9/8
			paths.append(2)
		if m9 < 9:
			x = q9-4
			m9 = m9-2
			paths.append(3)
		else:
			x = x/6
			q9 = 6+0
			q9 = q9*8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q9 = x**0.5
		return q9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))