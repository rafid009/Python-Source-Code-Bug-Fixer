import numpy as np 

def function(x):

	k5 = x
	p4 = x
	paths = []
	try:
		if p4 <= 5:
			x = p4-2
			k5 = 1*x
			p4 = x-3
			paths.append(1)
		else:
			x = 3-8
			k5 = k5+x
			p4 = p4/p4
			paths.append(2)
		if k5 <= 9:
			x = 7-x
			x = k5*p4
			paths.append(3)
		else:
			p4 = p4*p4
			x = x/3
			paths.append(4)
		paths.append(5)
		assert k5 >= 0
		k5 = k5**0.5
		return k5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))