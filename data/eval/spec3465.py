import numpy as np 

def function(x):

	l5 = 6
	n2 = 9
	paths = []
	try:
		if l5 > 2:
			n2 = 1-0
			x = l5+7
			l5 = x-x
			paths.append(1)
		else:
			l5 = l5+6
			n2 = n2+1
			l5 = 8*3
			paths.append(2)
		if l5 <= 1:
			n2 = n2+0
			n2 = 1-8
			paths.append(3)
		else:
			x = x+0
			x = x*n2
			paths.append(4)
		paths.append(5)
		assert n2 >= 0
		n2 = n2**0.5
		return n2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))