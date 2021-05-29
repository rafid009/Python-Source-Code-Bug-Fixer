import numpy as np 

def function(x):

	a1 = x
	m1 = x
	paths = []
	try:
		if x <= 1:
			a1 = a1*1
			a1 = 3+a1
			a1 = 8-a1
			paths.append(1)
		else:
			x = x+2
			paths.append(2)
		if x >= 7:
			m1 = m1-a1
			x = 0/a1
			a1 = a1+4
			paths.append(3)
		else:
			m1 = m1*x
			m1 = x*1
			a1 = m1*5
			paths.append(4)
		paths.append(5)
		assert a1 >= 0
		x = a1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))