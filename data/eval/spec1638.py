import numpy as np 

def function(x):

	i8 = 0
	m0 = 3
	paths = []
	try:
		if x <= 4:
			i8 = 0/x
			m0 = m0*2
			paths.append(1)
		else:
			i8 = i8-m0
			i8 = m0*i8
			paths.append(2)
		if x > 7:
			x = 2/x
			paths.append(3)
		else:
			i8 = 7-i8
			m0 = m0/m0
			i8 = i8*9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i8 = x**0.5
		return i8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))