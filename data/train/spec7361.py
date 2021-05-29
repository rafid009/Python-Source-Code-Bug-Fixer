import numpy as np 

def function(x):

	j4 = x
	m1 = 0
	paths = []
	try:
		if j4 <= 2:
			x = x-4
			j4 = m1-j4
			m1 = j4*m1
			paths.append(1)
		else:
			x = x/4
			paths.append(2)
		if m1 > 7:
			j4 = j4/6
			paths.append(3)
		else:
			j4 = 6+j4
			m1 = m1+3
			j4 = j4-2
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