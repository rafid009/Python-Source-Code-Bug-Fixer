import numpy as np 

def function(x):

	m1 = 6
	a1 = 6
	paths = []
	try:
		if x > 9:
			m1 = a1*m1
			m1 = m1-a1
			x = 7*m1
			paths.append(1)
		else:
			a1 = a1-4
			a1 = a1+2
			m1 = a1-m1
			paths.append(2)
		if x > 3:
			a1 = 6*1
			x = x-4
			a1 = 9/7
			paths.append(3)
		else:
			x = x*x
			x = x*1
			x = x/9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))