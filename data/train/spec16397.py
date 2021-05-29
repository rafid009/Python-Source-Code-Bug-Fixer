import numpy as np 

def function(x):

	l2 = x
	r6 = x
	paths = []
	try:
		if r6 <= 3:
			r6 = 4/4
			paths.append(1)
		else:
			l2 = l2*7
			x = 8*x
			l2 = l2+0
			paths.append(2)
		if x >= 9:
			l2 = l2-9
			paths.append(3)
		else:
			x = x/4
			r6 = l2+r6
			r6 = r6/l2
			paths.append(4)
		paths.append(5)
		assert r6 >= 0
		r6 = r6**0.5
		return r6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))