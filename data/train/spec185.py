import numpy as np 

def function(x):

	m4 = x
	p6 = 3
	paths = []
	try:
		if x > 1:
			m4 = 1-5
			paths.append(1)
		else:
			x = x+3
			p6 = p6/1
			paths.append(2)
		if x > 9:
			p6 = 0+7
			paths.append(3)
		else:
			x = x*9
			p6 = p6/9
			x = x+6
			paths.append(4)
		paths.append(5)
		assert m4 >= 0
		x = m4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))