import numpy as np 

def function(x):

	m7 = x
	a3 = x
	paths = []
	try:
		if x > 4:
			a3 = 5*a3
			paths.append(1)
		else:
			x = x+8
			m7 = m7*x
			paths.append(2)
		if m7 > 3:
			x = 7+4
			paths.append(3)
		else:
			a3 = a3-2
			paths.append(4)
		paths.append(5)
		assert a3 >= 0
		x = a3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))