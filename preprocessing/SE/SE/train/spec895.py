import numpy as np 

def function(x):

	p4 = 2
	j4 = x
	paths = []
	try:
		if p4 > 8:
			p4 = p4/p4
			paths.append(1)
		else:
			j4 = j4*1
			paths.append(2)
		if p4 < 6:
			p4 = 8/p4
			p4 = 0+p4
			paths.append(3)
		else:
			p4 = p4+9
			j4 = 6*j4
			paths.append(4)
		paths.append(5)
		assert j4 >= 0
		p4 = j4**0.5
		return p4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))