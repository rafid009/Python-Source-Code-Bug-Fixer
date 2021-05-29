import numpy as np 

def function(x):

	l3 = 2
	i1 = 2
	paths = []
	try:
		if x < 1:
			i1 = x-x
			i1 = i1-1
			l3 = l3+i1
			paths.append(1)
		else:
			i1 = 2*7
			x = 4/x
			l3 = l3+9
			paths.append(2)
		if l3 >= 3:
			i1 = 7+i1
			i1 = i1-1
			paths.append(3)
		else:
			l3 = i1/x
			x = x*2
			paths.append(4)
		paths.append(5)
		assert l3 >= 0
		i1 = l3**0.5
		return i1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))