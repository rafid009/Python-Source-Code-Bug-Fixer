import numpy as np 

def function(x):

	l3 = x
	b4 = 7
	paths = []
	try:
		if b4 >= 3:
			l3 = l3+9
			paths.append(1)
		else:
			b4 = 0+1
			l3 = 7*b4
			x = x+1
			paths.append(2)
		if b4 >= 8:
			l3 = l3/9
			b4 = b4/9
			l3 = l3*l3
			paths.append(3)
		else:
			l3 = l3-b4
			b4 = 0/b4
			paths.append(4)
		paths.append(5)
		assert l3 >= 0
		x = l3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))