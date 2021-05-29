import numpy as np 

def function(x):

	m8 = 4
	a7 = x
	paths = []
	try:
		if m8 < 8:
			m8 = x-6
			a7 = a7-8
			paths.append(1)
		else:
			a7 = x-a7
			x = 5*x
			a7 = 5+a7
			paths.append(2)
		if m8 < 1:
			x = a7+7
			m8 = 1/m8
			a7 = 3+m8
			paths.append(3)
		else:
			a7 = 0+2
			paths.append(4)
		paths.append(5)
		assert a7 >= 0
		a7 = a7**0.5
		return a7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))