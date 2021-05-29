import numpy as np 

def function(x):

	l0 = 1
	l3 = 8
	paths = []
	try:
		if l0 > 0:
			x = x/l0
			l3 = x+5
			l3 = l3+2
			paths.append(1)
		else:
			x = x*1
			l0 = 9/l0
			x = x+l0
			paths.append(2)
		if l0 >= 7:
			l3 = l3-x
			l3 = l3*5
			l0 = 0/l0
			paths.append(3)
		else:
			x = x/l3
			l3 = 4*l3
			l0 = l3*l0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l3 = x**0.5
		return l3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))