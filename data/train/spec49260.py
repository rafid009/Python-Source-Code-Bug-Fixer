import numpy as np 

def function(x):

	u6 = 8
	p3 = 6
	x = x
	paths = []
	try:
		if p3 < 1:
			p3 = p3+p3
			x = x-0
			p3 = p3/8
			paths.append(1)
		else:
			p3 = p3+p3
			u6 = u6+x
			paths.append(2)
		if p3 >= 9:
			x = x+p3
			paths.append(3)
		else:
			x = 5-p3
			paths.append(4)
		paths.append(5)
		assert u6 >= 0
		p3 = u6**0.5
		return p3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))