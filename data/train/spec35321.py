import numpy as np 

def function(x):

	i0 = x
	m1 = 8
	x = 7
	paths = []
	try:
		if x <= 1:
			i0 = 1+m1
			paths.append(1)
		else:
			i0 = i0+3
			paths.append(2)
		if i0 < 1:
			m1 = m1/3
			i0 = m1*i0
			paths.append(3)
		else:
			i0 = i0/6
			x = 6/4
			paths.append(4)
		paths.append(5)
		assert i0 >= 0
		x = i0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))