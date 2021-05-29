import numpy as np 

def function(x):

	j2 = 8
	p7 = x
	paths = []
	try:
		if x >= 2:
			p7 = 1/j2
			j2 = p7*j2
			j2 = 3-j2
			paths.append(1)
		else:
			j2 = j2-p7
			paths.append(2)
		if j2 > 4:
			x = 5*j2
			j2 = j2/6
			paths.append(3)
		else:
			x = 7*x
			paths.append(4)
		paths.append(5)
		assert p7 >= 0
		x = p7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))