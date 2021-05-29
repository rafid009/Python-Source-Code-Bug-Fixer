import numpy as np 

def function(x):

	p6 = x
	a1 = x
	paths = []
	try:
		if a1 > 5:
			x = a1+7
			a1 = a1*1
			p6 = a1*p6
			paths.append(1)
		else:
			a1 = x*a1
			p6 = p6*5
			x = x/a1
			paths.append(2)
		if a1 > 7:
			a1 = a1*a1
			paths.append(3)
		else:
			p6 = p6-7
			x = 0/x
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