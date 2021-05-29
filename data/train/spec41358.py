import numpy as np 

def function(x):

	e6 = 3
	p4 = x
	paths = []
	try:
		if p4 < 4:
			e6 = e6/p4
			e6 = 1-p4
			e6 = 3-x
			paths.append(1)
		else:
			p4 = 0*p4
			e6 = e6+p4
			x = x/1
			paths.append(2)
		if e6 >= 6:
			e6 = 5/p4
			p4 = 3-p4
			p4 = p4+7
			paths.append(3)
		else:
			p4 = x+3
			x = x/x
			x = x-9
			paths.append(4)
		paths.append(5)
		assert e6 >= 0
		p4 = e6**0.5
		return p4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))