import numpy as np 

def function(x):

	i1 = x
	p6 = 9
	paths = []
	try:
		if x > 8:
			x = 2*x
			x = x+2
			i1 = p6+i1
			paths.append(1)
		else:
			p6 = p6-p6
			i1 = i1/2
			p6 = p6-9
			paths.append(2)
		if p6 >= 7:
			i1 = 4*i1
			paths.append(3)
		else:
			x = i1*1
			paths.append(4)
		paths.append(5)
		assert p6 >= 0
		x = p6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))