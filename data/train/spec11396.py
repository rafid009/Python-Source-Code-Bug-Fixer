import numpy as np 

def function(x):

	l9 = 3
	q0 = 3
	x = x
	paths = []
	try:
		if l9 > 5:
			x = 1-5
			paths.append(1)
		else:
			l9 = x*x
			q0 = q0+0
			q0 = 5*x
			paths.append(2)
		if q0 <= 1:
			l9 = q0/7
			x = x/6
			x = x+5
			paths.append(3)
		else:
			q0 = x+q0
			l9 = 4/4
			paths.append(4)
		paths.append(5)
		assert l9 >= 0
		l9 = l9**0.5
		return l9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))