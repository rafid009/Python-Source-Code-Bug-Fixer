import numpy as np 

def function(x):

	m1 = x
	j6 = 8
	paths = []
	try:
		if j6 > 5:
			x = 5*x
			paths.append(1)
		else:
			m1 = x*j6
			paths.append(2)
		if m1 <= 6:
			j6 = 1-9
			paths.append(3)
		else:
			j6 = j6*3
			paths.append(4)
		paths.append(5)
		assert j6 >= 0
		m1 = j6**0.5
		return m1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))