import numpy as np 

def function(x):

	p4 = x
	m2 = x
	x = 4
	paths = []
	try:
		if p4 > 9:
			x = x-m2
			paths.append(1)
		else:
			m2 = 5+m2
			paths.append(2)
		if x < 6:
			p4 = 3+0
			x = x-2
			x = m2*x
			paths.append(3)
		else:
			x = 7-4
			paths.append(4)
		paths.append(5)
		assert m2 >= 0
		p4 = m2**0.5
		return p4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))