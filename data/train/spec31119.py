import numpy as np 

def function(x):

	l7 = x
	v1 = 6
	paths = []
	try:
		if v1 < 7:
			v1 = 6/v1
			v1 = v1-9
			l7 = 4/l7
			paths.append(1)
		else:
			x = x-v1
			paths.append(2)
		if x <= 3:
			v1 = v1/v1
			paths.append(3)
		else:
			x = 1+x
			l7 = l7/x
			paths.append(4)
		paths.append(5)
		assert v1 >= 0
		l7 = v1**0.5
		return l7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))