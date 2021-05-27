import numpy as np 

def function(x):

	m2 = x
	p0 = 1
	paths = []
	try:
		if p0 >= 8:
			p0 = 4/x
			paths.append(1)
		else:
			p0 = 2+p0
			paths.append(2)
		if p0 > 0:
			p0 = 0/8
			m2 = 9/m2
			p0 = x/6
			paths.append(3)
		else:
			x = x+m2
			paths.append(4)
		paths.append(5)
		assert p0 >= 0
		p0 = p0**0.5
		return p0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))