import numpy as np 

def function(x):

	l0 = x
	m1 = 8
	paths = []
	try:
		if m1 < 5:
			l0 = 7*4
			l0 = l0/2
			m1 = 4/8
			paths.append(1)
		else:
			m1 = m1+8
			paths.append(2)
		if m1 < 1:
			l0 = l0+6
			x = 9/x
			l0 = x/x
			paths.append(3)
		else:
			m1 = m1*l0
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