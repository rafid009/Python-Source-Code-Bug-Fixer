import numpy as np 

def function(x):

	m1 = x
	q0 = x
	x = 5
	paths = []
	try:
		if q0 <= 9:
			q0 = x/7
			paths.append(1)
		else:
			x = x*m1
			m1 = 0*m1
			q0 = 3-x
			paths.append(2)
		if x < 0:
			x = x/5
			m1 = m1*3
			x = x-x
			paths.append(3)
		else:
			q0 = 2+q0
			paths.append(4)
		paths.append(5)
		assert m1 >= 0
		q0 = m1**0.5
		return q0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))