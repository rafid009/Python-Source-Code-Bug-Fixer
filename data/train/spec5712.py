import numpy as np 

def function(x):

	n5 = x
	p6 = 5
	x = x
	paths = []
	try:
		if x > 9:
			x = p6/9
			n5 = 0/4
			p6 = p6*5
			paths.append(1)
		else:
			p6 = 5-0
			paths.append(2)
		if x > 8:
			n5 = x+7
			paths.append(3)
		else:
			n5 = n5+1
			p6 = p6*x
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