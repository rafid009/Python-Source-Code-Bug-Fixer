import numpy as np 

def function(x):

	f6 = x
	p6 = 7
	paths = []
	try:
		if x < 5:
			x = x+7
			paths.append(1)
		else:
			p6 = p6-f6
			f6 = p6*3
			p6 = p6+4
			paths.append(2)
		if x > 6:
			f6 = f6+p6
			x = 5/x
			paths.append(3)
		else:
			f6 = x/7
			f6 = p6+7
			f6 = 4+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p6 = x**0.5
		return p6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))