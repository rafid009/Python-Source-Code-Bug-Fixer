import numpy as np 

def function(x):

	j4 = 6
	m1 = 1
	paths = []
	try:
		if m1 >= 6:
			m1 = 5+j4
			paths.append(1)
		else:
			j4 = j4-9
			m1 = 9/6
			m1 = j4/m1
			paths.append(2)
		if j4 < 5:
			m1 = m1*2
			j4 = j4-0
			paths.append(3)
		else:
			x = 8*x
			x = j4-x
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