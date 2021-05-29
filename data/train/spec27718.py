import numpy as np 

def function(x):

	u6 = 1
	p1 = 7
	paths = []
	try:
		if p1 <= 5:
			u6 = u6*2
			p1 = u6+p1
			paths.append(1)
		else:
			u6 = u6+3
			x = x+u6
			p1 = p1+p1
			paths.append(2)
		if u6 <= 9:
			u6 = x+4
			paths.append(3)
		else:
			u6 = 0-u6
			p1 = 4*p1
			paths.append(4)
		paths.append(5)
		assert u6 >= 0
		u6 = u6**0.5
		return u6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))