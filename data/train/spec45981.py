import numpy as np 

def function(x):

	m1 = x
	j4 = x
	paths = []
	try:
		if x < 2:
			m1 = x-4
			j4 = 2-j4
			paths.append(1)
		else:
			j4 = j4/x
			j4 = 0-j4
			paths.append(2)
		if m1 <= 4:
			m1 = 5-9
			x = 8-5
			paths.append(3)
		else:
			j4 = j4-6
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