import numpy as np 

def function(x):

	m5 = 3
	i1 = 2
	paths = []
	try:
		if x >= 0:
			i1 = m5-4
			paths.append(1)
		else:
			m5 = 9/2
			m5 = m5*4
			paths.append(2)
		if m5 <= 7:
			i1 = x-5
			paths.append(3)
		else:
			x = x-0
			m5 = 9-7
			paths.append(4)
		paths.append(5)
		assert i1 >= 0
		x = i1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))