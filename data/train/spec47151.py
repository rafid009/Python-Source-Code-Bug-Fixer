import numpy as np 

def function(x):

	u3 = x
	l5 = x
	paths = []
	try:
		if x > 1:
			u3 = u3+x
			paths.append(1)
		else:
			x = l5-9
			paths.append(2)
		if l5 < 4:
			x = x+1
			paths.append(3)
		else:
			l5 = 3/l5
			paths.append(4)
		paths.append(5)
		assert l5 >= 0
		l5 = l5**0.5
		return l5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))