import numpy as np 

def function(x):

	r1 = x
	l3 = x
	paths = []
	try:
		if l3 >= 5:
			x = r1-x
			r1 = 9+r1
			l3 = 4/8
			paths.append(1)
		else:
			r1 = 6-r1
			r1 = r1-x
			paths.append(2)
		if l3 < 8:
			r1 = r1/2
			paths.append(3)
		else:
			l3 = l3+l3
			r1 = r1/4
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