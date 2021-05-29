import numpy as np 

def function(x):

	m6 = x
	m2 = x
	paths = []
	try:
		if m2 < 8:
			m6 = x/m2
			x = x-4
			m2 = m2*4
			paths.append(1)
		else:
			m2 = 1+m2
			m6 = m6/3
			m2 = m6+m2
			paths.append(2)
		if m6 > 7:
			m2 = 9/m2
			m2 = 1+9
			paths.append(3)
		else:
			m2 = m2/m6
			m6 = m2/1
			paths.append(4)
		paths.append(5)
		assert m2 >= 0
		x = m2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))