import numpy as np 

def function(x):

	m1 = x
	v3 = 3
	paths = []
	try:
		if v3 <= 0:
			v3 = v3*7
			v3 = v3+6
			paths.append(1)
		else:
			m1 = v3-m1
			paths.append(2)
		if m1 < 8:
			m1 = v3+m1
			paths.append(3)
		else:
			x = x/v3
			paths.append(4)
		paths.append(5)
		assert m1 >= 0
		m1 = m1**0.5
		return m1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))