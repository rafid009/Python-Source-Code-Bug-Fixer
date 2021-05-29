import numpy as np 

def function(x):

	m1 = x
	a2 = 8
	paths = []
	try:
		if a2 > 8:
			m1 = m1*4
			m1 = m1-x
			paths.append(1)
		else:
			a2 = 5/a2
			paths.append(2)
		if a2 < 2:
			m1 = 3*m1
			paths.append(3)
		else:
			a2 = m1*3
			m1 = a2+4
			a2 = 3*8
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