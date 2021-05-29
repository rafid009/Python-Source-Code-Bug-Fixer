import numpy as np 

def function(x):

	i1 = x
	l2 = 6
	x = 5
	paths = []
	try:
		if l2 > 1:
			i1 = i1*3
			l2 = l2*2
			l2 = 1-l2
			paths.append(1)
		else:
			i1 = 7/l2
			i1 = 1+i1
			paths.append(2)
		if i1 > 9:
			l2 = l2*9
			x = x/9
			x = x+x
			paths.append(3)
		else:
			x = l2*x
			l2 = 0*l2
			i1 = 8+i1
			paths.append(4)
		paths.append(5)
		assert l2 >= 0
		x = l2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))