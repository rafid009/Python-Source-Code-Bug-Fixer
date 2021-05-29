import numpy as np 

def function(x):

	p6 = x
	l1 = x
	paths = []
	try:
		if l1 > 2:
			l1 = 6/7
			x = x-5
			l1 = 2*l1
			paths.append(1)
		else:
			l1 = l1*0
			paths.append(2)
		if x < 7:
			p6 = 9/p6
			x = x*7
			l1 = 9+l1
			paths.append(3)
		else:
			l1 = 2-3
			p6 = 4-p6
			paths.append(4)
		paths.append(5)
		assert p6 >= 0
		x = p6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))