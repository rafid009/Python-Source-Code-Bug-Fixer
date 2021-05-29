import numpy as np 

def function(x):

	a6 = 7
	m5 = x
	paths = []
	try:
		if x >= 0:
			m5 = m5/4
			paths.append(1)
		else:
			x = 3-a6
			m5 = m5/5
			paths.append(2)
		if m5 >= 1:
			a6 = 6/a6
			m5 = 7/7
			x = 1/1
			paths.append(3)
		else:
			m5 = m5*8
			a6 = a6-m5
			paths.append(4)
		paths.append(5)
		assert a6 >= 0
		a6 = a6**0.5
		return a6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))