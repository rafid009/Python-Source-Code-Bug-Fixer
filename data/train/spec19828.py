import numpy as np 

def function(x):

	m1 = 3
	v9 = 0
	paths = []
	try:
		if m1 <= 3:
			m1 = 6*x
			paths.append(1)
		else:
			m1 = m1+m1
			m1 = 5/4
			m1 = 4/6
			paths.append(2)
		if v9 >= 3:
			m1 = 0/m1
			paths.append(3)
		else:
			v9 = v9*x
			v9 = 0-5
			paths.append(4)
		paths.append(5)
		assert v9 >= 0
		x = v9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))