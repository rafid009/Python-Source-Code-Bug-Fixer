import numpy as np 

def function(x):

	p1 = x
	j6 = 1
	paths = []
	try:
		if j6 > 2:
			j6 = j6+j6
			j6 = j6-4
			paths.append(1)
		else:
			p1 = p1-7
			x = 5+2
			j6 = j6-8
			paths.append(2)
		if j6 < 6:
			x = p1-j6
			paths.append(3)
		else:
			p1 = 2*p1
			j6 = 1/j6
			paths.append(4)
		paths.append(5)
		assert j6 >= 0
		x = j6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))