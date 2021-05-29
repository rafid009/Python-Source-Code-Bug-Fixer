import numpy as np 

def function(x):

	x5 = x
	m1 = x
	paths = []
	try:
		if m1 <= 7:
			m1 = 3/9
			x = 8/9
			x = m1/x5
			paths.append(1)
		else:
			m1 = 1*m1
			x = x*m1
			paths.append(2)
		if x5 > 9:
			x5 = x5-x
			m1 = m1-6
			x5 = 8/x
			paths.append(3)
		else:
			m1 = m1-3
			x = 5/x
			m1 = x5+m1
			paths.append(4)
		paths.append(5)
		assert m1 >= 0
		x = m1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))