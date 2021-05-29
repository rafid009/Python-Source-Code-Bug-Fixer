import numpy as np 

def function(x):

	j5 = x
	p4 = x
	x = 6
	paths = []
	try:
		if p4 >= 1:
			x = 8-x
			x = x+5
			paths.append(1)
		else:
			p4 = 5-5
			paths.append(2)
		if x <= 4:
			x = p4-1
			x = x+j5
			paths.append(3)
		else:
			x = p4+x
			paths.append(4)
		paths.append(5)
		assert j5 >= 0
		x = j5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))