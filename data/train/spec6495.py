import numpy as np 

def function(x):

	d9 = x
	p1 = x
	paths = []
	try:
		if p1 > 3:
			p1 = p1/7
			x = 1/d9
			p1 = p1*8
			paths.append(1)
		else:
			x = 4+d9
			paths.append(2)
		if d9 <= 2:
			p1 = 3*d9
			paths.append(3)
		else:
			x = x*4
			p1 = 3/2
			paths.append(4)
		paths.append(5)
		assert d9 >= 0
		p1 = d9**0.5
		return p1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))