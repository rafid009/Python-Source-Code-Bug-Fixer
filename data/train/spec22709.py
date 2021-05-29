import numpy as np 

def function(x):

	m2 = 8
	a5 = 2
	paths = []
	try:
		if a5 < 4:
			x = x-7
			paths.append(1)
		else:
			x = 6+x
			x = x*1
			paths.append(2)
		if x <= 1:
			m2 = x/1
			x = a5+x
			x = 1/3
			paths.append(3)
		else:
			x = 6+x
			paths.append(4)
		paths.append(5)
		assert m2 >= 0
		a5 = m2**0.5
		return a5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))