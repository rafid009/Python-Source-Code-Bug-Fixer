import numpy as np 

def function(x):

	p6 = x
	r1 = 2
	paths = []
	try:
		if r1 > 3:
			x = 3*1
			p6 = p6*r1
			paths.append(1)
		else:
			x = x/r1
			x = x*9
			x = 9/x
			paths.append(2)
		if p6 >= 4:
			p6 = 2-r1
			p6 = p6+8
			paths.append(3)
		else:
			x = x*x
			paths.append(4)
		paths.append(5)
		assert p6 >= 0
		p6 = p6**0.5
		return p6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))