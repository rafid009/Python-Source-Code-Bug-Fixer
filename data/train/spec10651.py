import numpy as np 

def function(x):

	p4 = x
	i5 = 3
	x = 8
	paths = []
	try:
		if x < 6:
			x = 6+x
			paths.append(1)
		else:
			p4 = 1-x
			x = 3-x
			paths.append(2)
		if i5 <= 7:
			i5 = 0-i5
			paths.append(3)
		else:
			p4 = 0*p4
			paths.append(4)
		paths.append(5)
		assert p4 >= 0
		i5 = p4**0.5
		return i5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))