import numpy as np 

def function(x):

	l2 = 9
	m1 = x
	paths = []
	try:
		if m1 > 4:
			l2 = l2/4
			paths.append(1)
		else:
			x = 7+x
			m1 = 5/m1
			paths.append(2)
		if x <= 4:
			m1 = 7-m1
			x = 7-2
			l2 = x-9
			paths.append(3)
		else:
			x = x/2
			l2 = 5-l2
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