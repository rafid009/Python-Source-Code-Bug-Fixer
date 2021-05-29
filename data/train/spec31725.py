import numpy as np 

def function(x):

	p6 = x
	j8 = 7
	paths = []
	try:
		if p6 >= 5:
			j8 = 6-j8
			paths.append(1)
		else:
			j8 = 4+5
			paths.append(2)
		if p6 >= 6:
			j8 = 6+j8
			j8 = j8-p6
			paths.append(3)
		else:
			j8 = 9-4
			x = x+3
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