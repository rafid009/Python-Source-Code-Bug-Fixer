import numpy as np 

def function(x):

	q9 = x
	m7 = x
	paths = []
	try:
		if x >= 1:
			q9 = q9*6
			q9 = q9*5
			paths.append(1)
		else:
			x = x*4
			q9 = 7-q9
			paths.append(2)
		if q9 >= 3:
			x = m7+x
			x = 1-x
			m7 = m7-2
			paths.append(3)
		else:
			q9 = q9*0
			m7 = 1*6
			paths.append(4)
		paths.append(5)
		assert m7 >= 0
		q9 = m7**0.5
		return q9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))