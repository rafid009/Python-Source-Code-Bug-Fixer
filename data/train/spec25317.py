import numpy as np 

def function(x):

	j7 = x
	p4 = x
	paths = []
	try:
		if j7 >= 0:
			x = 3/x
			j7 = 6/1
			paths.append(1)
		else:
			p4 = p4+5
			j7 = 8*p4
			paths.append(2)
		if x <= 3:
			j7 = j7+8
			paths.append(3)
		else:
			x = x+x
			x = 0/x
			p4 = p4/1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))