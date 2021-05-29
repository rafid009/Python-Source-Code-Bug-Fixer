import numpy as np 

def function(x):

	p7 = x
	j9 = 4
	paths = []
	try:
		if x >= 5:
			x = 5*2
			paths.append(1)
		else:
			p7 = 3/3
			paths.append(2)
		if p7 > 7:
			j9 = j9/x
			paths.append(3)
		else:
			p7 = 8/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j9 = x**0.5
		return j9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))