import numpy as np 

def function(x):

	m4 = 2
	j4 = x
	paths = []
	try:
		if j4 < 8:
			x = 3-8
			j4 = j4/m4
			j4 = 2-9
			paths.append(1)
		else:
			j4 = j4/5
			m4 = 8/9
			m4 = j4-j4
			paths.append(2)
		if x <= 4:
			j4 = j4-5
			m4 = m4-7
			paths.append(3)
		else:
			m4 = m4/8
			x = x-8
			j4 = j4/j4
			paths.append(4)
		paths.append(5)
		assert m4 >= 0
		x = m4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))