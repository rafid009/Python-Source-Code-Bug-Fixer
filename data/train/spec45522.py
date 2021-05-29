import numpy as np 

def function(x):

	l3 = 9
	p0 = 0
	paths = []
	try:
		if x > 0:
			p0 = 8+p0
			paths.append(1)
		else:
			x = x*4
			paths.append(2)
		if l3 <= 2:
			p0 = l3*8
			l3 = 1*3
			paths.append(3)
		else:
			x = x+7
			l3 = l3-8
			l3 = x*l3
			paths.append(4)
		paths.append(5)
		assert l3 >= 0
		p0 = l3**0.5
		return p0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))