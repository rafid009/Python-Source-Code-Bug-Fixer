import numpy as np 

def function(x):

	m1 = x
	q7 = 8
	paths = []
	try:
		if m1 > 9:
			q7 = q7+x
			x = x*m1
			paths.append(1)
		else:
			q7 = 1+q7
			paths.append(2)
		if x > 0:
			x = 8+7
			m1 = m1-m1
			paths.append(3)
		else:
			q7 = x/3
			m1 = q7*1
			paths.append(4)
		paths.append(5)
		assert q7 >= 0
		x = q7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))