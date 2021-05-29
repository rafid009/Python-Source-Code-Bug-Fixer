import numpy as np 

def function(x):

	p1 = 3
	v7 = x
	paths = []
	try:
		if x < 4:
			x = x-5
			x = v7*v7
			paths.append(1)
		else:
			v7 = 9/7
			p1 = p1/1
			p1 = x/p1
			paths.append(2)
		if v7 >= 0:
			p1 = 4-0
			paths.append(3)
		else:
			p1 = p1-3
			paths.append(4)
		paths.append(5)
		assert v7 >= 0
		v7 = v7**0.5
		return v7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))