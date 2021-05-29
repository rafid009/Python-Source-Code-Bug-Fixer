import numpy as np 

def function(x):

	m1 = x
	d5 = x
	paths = []
	try:
		if m1 > 3:
			d5 = 8-d5
			m1 = 0+7
			paths.append(1)
		else:
			d5 = d5-d5
			paths.append(2)
		if x > 3:
			m1 = m1+m1
			d5 = 9*m1
			paths.append(3)
		else:
			d5 = d5+3
			m1 = 2/m1
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