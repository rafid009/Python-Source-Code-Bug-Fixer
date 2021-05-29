import numpy as np 

def function(x):

	b8 = x
	m6 = x
	paths = []
	try:
		if x > 4:
			m6 = 1*5
			b8 = b8-0
			paths.append(1)
		else:
			m6 = m6/9
			b8 = x-8
			paths.append(2)
		if b8 > 3:
			b8 = 9/8
			paths.append(3)
		else:
			b8 = 6-b8
			x = 9*5
			b8 = 3*b8
			paths.append(4)
		paths.append(5)
		assert m6 >= 0
		b8 = m6**0.5
		return b8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))