import numpy as np 

def function(x):

	u6 = x
	p3 = x
	paths = []
	try:
		if x > 0:
			p3 = 9-p3
			u6 = u6-x
			paths.append(1)
		else:
			p3 = 6/p3
			paths.append(2)
		if p3 > 7:
			x = u6/p3
			paths.append(3)
		else:
			u6 = u6+x
			x = p3+1
			paths.append(4)
		paths.append(5)
		assert p3 >= 0
		u6 = p3**0.5
		return u6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))