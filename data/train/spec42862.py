import numpy as np 

def function(x):

	p3 = 1
	i5 = x
	paths = []
	try:
		if p3 > 2:
			p3 = p3/p3
			x = x+7
			paths.append(1)
		else:
			i5 = i5*9
			i5 = p3*i5
			i5 = 2/i5
			paths.append(2)
		if x >= 2:
			p3 = 4+1
			x = i5*7
			paths.append(3)
		else:
			p3 = p3*7
			p3 = 4/p3
			paths.append(4)
		paths.append(5)
		assert i5 >= 0
		i5 = i5**0.5
		return i5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))