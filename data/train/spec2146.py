import numpy as np 

def function(x):

	u3 = 8
	l1 = x
	paths = []
	try:
		if l1 < 7:
			u3 = 2/2
			u3 = u3/4
			paths.append(1)
		else:
			l1 = l1/2
			l1 = l1/8
			paths.append(2)
		if l1 > 7:
			x = l1-x
			u3 = 8+1
			x = x*1
			paths.append(3)
		else:
			u3 = u3/x
			paths.append(4)
		paths.append(5)
		assert l1 >= 0
		x = l1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))