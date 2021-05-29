import numpy as np 

def function(x):

	m3 = 9
	q2 = x
	paths = []
	try:
		if x > 4:
			q2 = q2/m3
			x = x-6
			paths.append(1)
		else:
			q2 = 2/q2
			x = m3+x
			m3 = 8/q2
			paths.append(2)
		if q2 > 0:
			q2 = q2+4
			paths.append(3)
		else:
			m3 = 0+m3
			q2 = 6*x
			x = x+2
			paths.append(4)
		paths.append(5)
		assert q2 >= 0
		q2 = q2**0.5
		return q2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))