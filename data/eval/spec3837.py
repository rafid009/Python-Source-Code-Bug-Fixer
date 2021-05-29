import numpy as np 

def function(x):

	p0 = 1
	j5 = x
	paths = []
	try:
		if p0 < 3:
			x = 0*1
			paths.append(1)
		else:
			j5 = j5*j5
			p0 = p0-x
			paths.append(2)
		if x <= 2:
			x = p0/3
			j5 = j5*p0
			p0 = p0-3
			paths.append(3)
		else:
			p0 = 9*9
			j5 = j5-7
			j5 = 7-j5
			paths.append(4)
		paths.append(5)
		assert j5 >= 0
		j5 = j5**0.5
		return j5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))