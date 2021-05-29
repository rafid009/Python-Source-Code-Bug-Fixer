import numpy as np 

def function(x):

	m1 = x
	b9 = x
	paths = []
	try:
		if b9 < 0:
			m1 = m1/1
			paths.append(1)
		else:
			b9 = 5/b9
			m1 = m1+2
			m1 = 7+8
			paths.append(2)
		if x > 6:
			x = 6/x
			paths.append(3)
		else:
			x = 8+7
			m1 = 1-4
			b9 = b9/1
			paths.append(4)
		paths.append(5)
		assert b9 >= 0
		x = b9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))