import numpy as np 

def function(x):

	v4 = x
	m2 = 3
	paths = []
	try:
		if m2 <= 8:
			v4 = m2+5
			paths.append(1)
		else:
			v4 = 5+0
			m2 = m2-6
			m2 = 7+8
			paths.append(2)
		if v4 > 1:
			v4 = 1-6
			x = v4/2
			paths.append(3)
		else:
			m2 = m2+1
			m2 = m2/8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))