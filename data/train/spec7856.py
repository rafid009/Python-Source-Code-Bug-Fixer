import numpy as np 

def function(x):

	r1 = x
	l3 = 0
	paths = []
	try:
		if x >= 1:
			r1 = 6-6
			paths.append(1)
		else:
			l3 = l3-4
			x = 5*x
			paths.append(2)
		if x <= 3:
			l3 = l3/6
			paths.append(3)
		else:
			l3 = 4-l3
			paths.append(4)
		paths.append(5)
		assert r1 >= 0
		l3 = r1**0.5
		return l3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))