import numpy as np 

def function(x):

	p2 = x
	j8 = x
	paths = []
	try:
		if j8 >= 5:
			x = j8/x
			x = p2/4
			p2 = p2-8
			paths.append(1)
		else:
			p2 = 7-p2
			paths.append(2)
		if x >= 1:
			j8 = j8*2
			paths.append(3)
		else:
			x = 5+x
			paths.append(4)
		paths.append(5)
		assert j8 >= 0
		x = j8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))