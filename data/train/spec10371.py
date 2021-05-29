import numpy as np 

def function(x):

	r9 = x
	l2 = 5
	x = 1
	paths = []
	try:
		if x <= 4:
			x = x+6
			paths.append(1)
		else:
			x = 7/1
			r9 = r9+x
			paths.append(2)
		if l2 > 2:
			l2 = 9-5
			x = 6*9
			paths.append(3)
		else:
			l2 = 4-l2
			l2 = l2+l2
			l2 = 1*l2
			paths.append(4)
		paths.append(5)
		assert r9 >= 0
		r9 = r9**0.5
		return r9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))