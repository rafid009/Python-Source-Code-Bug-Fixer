import numpy as np 

def function(x):

	l4 = x
	r6 = 0
	paths = []
	try:
		if x < 9:
			r6 = 5/8
			r6 = r6-4
			paths.append(1)
		else:
			x = x-x
			l4 = r6+x
			l4 = l4/4
			paths.append(2)
		if l4 >= 0:
			l4 = l4+l4
			paths.append(3)
		else:
			l4 = l4+r6
			paths.append(4)
		paths.append(5)
		assert r6 >= 0
		l4 = r6**0.5
		return l4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))