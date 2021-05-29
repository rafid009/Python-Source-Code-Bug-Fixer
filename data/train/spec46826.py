import numpy as np 

def function(x):

	p6 = 4
	m1 = x
	x = x
	paths = []
	try:
		if x < 8:
			m1 = m1-7
			x = m1+x
			m1 = m1/7
			paths.append(1)
		else:
			x = x/6
			paths.append(2)
		if x >= 4:
			x = 2*x
			x = x+5
			p6 = p6+2
			paths.append(3)
		else:
			x = 8/9
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