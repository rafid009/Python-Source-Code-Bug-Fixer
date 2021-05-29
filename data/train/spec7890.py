import numpy as np 

def function(x):

	m5 = 1
	l1 = x
	paths = []
	try:
		if l1 < 8:
			m5 = 5*x
			paths.append(1)
		else:
			m5 = m5+m5
			m5 = 4/1
			x = x-m5
			paths.append(2)
		if l1 > 5:
			m5 = x-1
			paths.append(3)
		else:
			l1 = 7/l1
			l1 = l1*8
			paths.append(4)
		paths.append(5)
		assert m5 >= 0
		x = m5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))