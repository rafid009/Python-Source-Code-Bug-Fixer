import numpy as np 

def function(x):

	l7 = x
	r6 = x
	paths = []
	try:
		if x > 5:
			r6 = r6+r6
			r6 = 8*r6
			r6 = x*r6
			paths.append(1)
		else:
			r6 = r6/2
			paths.append(2)
		if r6 <= 2:
			x = x/l7
			l7 = l7/l7
			paths.append(3)
		else:
			x = r6/5
			x = x*x
			l7 = x-l7
			paths.append(4)
		paths.append(5)
		assert l7 >= 0
		l7 = l7**0.5
		return l7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))