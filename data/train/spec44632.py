import numpy as np 

def function(x):

	a0 = x
	m6 = 9
	paths = []
	try:
		if a0 >= 1:
			a0 = a0+7
			a0 = 9/1
			paths.append(1)
		else:
			x = x+a0
			x = x+5
			paths.append(2)
		if a0 < 5:
			m6 = m6*m6
			x = x-m6
			x = x-8
			paths.append(3)
		else:
			x = x+x
			m6 = 3/m6
			paths.append(4)
		paths.append(5)
		assert a0 >= 0
		x = a0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))