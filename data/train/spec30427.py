import numpy as np 

def function(x):

	a2 = x
	m1 = 7
	paths = []
	try:
		if x > 1:
			m1 = 3-m1
			m1 = x/m1
			paths.append(1)
		else:
			a2 = 2*a2
			m1 = 9+m1
			m1 = 3/x
			paths.append(2)
		if m1 >= 3:
			a2 = 4-a2
			x = x-6
			a2 = a2/1
			paths.append(3)
		else:
			m1 = a2/8
			x = 4+a2
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