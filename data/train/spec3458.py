import numpy as np 

def function(x):

	m1 = x
	k5 = 3
	x = x
	paths = []
	try:
		if m1 >= 0:
			x = 7/x
			k5 = x/1
			paths.append(1)
		else:
			x = x-7
			x = 5*x
			m1 = m1/3
			paths.append(2)
		if k5 > 7:
			x = x/3
			m1 = m1*m1
			x = x+m1
			paths.append(3)
		else:
			k5 = k5/8
			x = x/8
			paths.append(4)
		paths.append(5)
		assert m1 >= 0
		x = m1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))