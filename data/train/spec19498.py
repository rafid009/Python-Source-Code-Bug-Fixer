import numpy as np 

def function(x):

	a6 = 1
	p1 = 3
	paths = []
	try:
		if x <= 9:
			a6 = a6-4
			p1 = 8-p1
			paths.append(1)
		else:
			a6 = a6+a6
			x = 5/x
			p1 = 8/a6
			paths.append(2)
		if p1 >= 7:
			p1 = p1+p1
			p1 = 8+7
			p1 = 9-6
			paths.append(3)
		else:
			a6 = a6/x
			p1 = 9-5
			paths.append(4)
		paths.append(5)
		assert a6 >= 0
		a6 = a6**0.5
		return a6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))