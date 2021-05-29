import numpy as np 

def function(x):

	m2 = x
	a3 = 6
	paths = []
	try:
		if m2 > 4:
			m2 = x/x
			x = 4+5
			a3 = a3-8
			paths.append(1)
		else:
			a3 = a3-m2
			m2 = m2*a3
			m2 = 6*m2
			paths.append(2)
		if x >= 7:
			m2 = m2-1
			m2 = m2*a3
			paths.append(3)
		else:
			m2 = 8/m2
			x = 5+7
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