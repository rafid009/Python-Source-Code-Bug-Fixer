import numpy as np 

def function(x):

	m1 = 4
	b1 = 7
	paths = []
	try:
		if m1 < 5:
			m1 = m1-m1
			paths.append(1)
		else:
			x = x+1
			paths.append(2)
		if b1 > 1:
			b1 = 2-9
			paths.append(3)
		else:
			m1 = m1*6
			paths.append(4)
		paths.append(5)
		assert b1 >= 0
		x = b1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))