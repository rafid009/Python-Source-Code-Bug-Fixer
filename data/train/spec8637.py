import numpy as np 

def function(x):

	m9 = x
	q7 = 6
	paths = []
	try:
		if q7 < 4:
			x = 9*0
			q7 = 0*m9
			paths.append(1)
		else:
			x = x-q7
			x = m9+x
			paths.append(2)
		if q7 > 8:
			x = 8-m9
			m9 = m9/q7
			q7 = 4*0
			paths.append(3)
		else:
			q7 = q7*7
			q7 = 5-q7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q7 = x**0.5
		return q7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))