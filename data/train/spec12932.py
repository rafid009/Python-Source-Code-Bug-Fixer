import numpy as np 

def function(x):

	p1 = x
	i5 = 2
	paths = []
	try:
		if x > 5:
			i5 = 1/i5
			paths.append(1)
		else:
			p1 = p1+2
			paths.append(2)
		if i5 < 5:
			p1 = 9-p1
			paths.append(3)
		else:
			i5 = 4/i5
			paths.append(4)
		paths.append(5)
		assert p1 >= 0
		p1 = p1**0.5
		return p1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))