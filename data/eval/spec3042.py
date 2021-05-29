import numpy as np 

def function(x):

	b6 = x
	m1 = x
	paths = []
	try:
		if m1 <= 8:
			b6 = 6/x
			m1 = 3-m1
			paths.append(1)
		else:
			b6 = x+b6
			m1 = m1*b6
			m1 = 8-m1
			paths.append(2)
		if m1 >= 8:
			m1 = 7-x
			b6 = b6/9
			m1 = m1+0
			paths.append(3)
		else:
			b6 = 0/8
			m1 = m1-m1
			paths.append(4)
		paths.append(5)
		assert b6 >= 0
		x = b6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))