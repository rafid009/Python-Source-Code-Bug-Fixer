import numpy as np 

def function(x):

	k4 = x
	l3 = 3
	paths = []
	try:
		if l3 <= 1:
			l3 = 4*l3
			l3 = 3-7
			k4 = k4*1
			paths.append(1)
		else:
			l3 = l3/k4
			k4 = l3+8
			paths.append(2)
		if x >= 7:
			l3 = l3/3
			paths.append(3)
		else:
			k4 = 8-8
			k4 = 1*k4
			l3 = l3*2
			paths.append(4)
		paths.append(5)
		assert l3 >= 0
		l3 = l3**0.5
		return l3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))