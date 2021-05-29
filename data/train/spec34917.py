import numpy as np 

def function(x):

	i1 = 9
	x2 = x
	paths = []
	try:
		if i1 > 9:
			x = x+0
			x = 1*x
			i1 = 0/i1
			paths.append(1)
		else:
			i1 = i1/4
			x = x*x
			i1 = 9+i1
			paths.append(2)
		if x2 <= 2:
			x2 = x2*x2
			x = 0/8
			i1 = 0/i1
			paths.append(3)
		else:
			x2 = 2-x2
			i1 = x2-i1
			i1 = i1+1
			paths.append(4)
		paths.append(5)
		assert i1 >= 0
		x2 = i1**0.5
		return x2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))