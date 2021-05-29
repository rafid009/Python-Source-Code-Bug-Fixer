import numpy as np 

def function(x):

	a0 = x
	m7 = 7
	x = 1
	paths = []
	try:
		if m7 >= 5:
			a0 = 7*6
			m7 = m7-9
			x = 6-x
			paths.append(1)
		else:
			a0 = a0/5
			x = a0*m7
			paths.append(2)
		if x > 0:
			a0 = a0*5
			m7 = m7-0
			m7 = m7-6
			paths.append(3)
		else:
			m7 = a0/3
			paths.append(4)
		paths.append(5)
		assert m7 >= 0
		x = m7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))