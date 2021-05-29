import numpy as np 

def function(x):

	u6 = x
	l3 = 6
	paths = []
	try:
		if u6 >= 5:
			l3 = l3/3
			l3 = x/1
			l3 = l3+2
			paths.append(1)
		else:
			x = 7/x
			paths.append(2)
		if l3 >= 8:
			u6 = 0-x
			paths.append(3)
		else:
			x = x-2
			x = u6/5
			u6 = x/u6
			paths.append(4)
		paths.append(5)
		assert u6 >= 0
		l3 = u6**0.5
		return l3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))