import numpy as np 

def function(x):

	m7 = x
	e8 = 0
	paths = []
	try:
		if x >= 0:
			e8 = e8/9
			paths.append(1)
		else:
			m7 = 6+9
			x = x-6
			e8 = e8+2
			paths.append(2)
		if e8 >= 3:
			m7 = 1+m7
			x = x-4
			paths.append(3)
		else:
			m7 = m7-8
			e8 = e8*x
			paths.append(4)
		paths.append(5)
		assert e8 >= 0
		x = e8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))