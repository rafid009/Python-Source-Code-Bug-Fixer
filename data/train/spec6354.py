import numpy as np 

def function(x):

	v1 = 3
	l1 = x
	paths = []
	try:
		if l1 >= 7:
			x = 1/x
			l1 = l1*l1
			paths.append(1)
		else:
			v1 = v1-2
			l1 = 5+v1
			l1 = l1+6
			paths.append(2)
		if l1 > 3:
			x = x/v1
			v1 = v1+x
			paths.append(3)
		else:
			l1 = l1/3
			x = x*v1
			paths.append(4)
		paths.append(5)
		assert v1 >= 0
		l1 = v1**0.5
		return l1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))