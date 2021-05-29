import numpy as np 

def function(x):

	p8 = x
	m1 = 0
	paths = []
	try:
		if m1 < 1:
			x = p8*x
			paths.append(1)
		else:
			x = p8/x
			paths.append(2)
		if m1 <= 1:
			x = x-4
			p8 = x*6
			paths.append(3)
		else:
			m1 = m1*2
			x = 4/x
			paths.append(4)
		paths.append(5)
		assert p8 >= 0
		p8 = p8**0.5
		return p8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))