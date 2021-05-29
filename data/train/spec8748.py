import numpy as np 

def function(x):

	m2 = 9
	q2 = 2
	paths = []
	try:
		if m2 < 8:
			x = 3+x
			m2 = 6*q2
			x = 2-5
			paths.append(1)
		else:
			x = q2+x
			paths.append(2)
		if x >= 5:
			m2 = 4-m2
			x = 2*x
			x = x+1
			paths.append(3)
		else:
			q2 = q2+3
			x = 8/9
			q2 = q2*m2
			paths.append(4)
		paths.append(5)
		assert m2 >= 0
		q2 = m2**0.5
		return q2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))