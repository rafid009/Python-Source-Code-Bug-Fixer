import numpy as np 

def function(x):

	l1 = x
	f3 = 8
	paths = []
	try:
		if l1 >= 4:
			f3 = f3+0
			paths.append(1)
		else:
			l1 = l1+x
			f3 = f3*9
			paths.append(2)
		if f3 >= 9:
			f3 = 8-f3
			l1 = l1/l1
			paths.append(3)
		else:
			f3 = 6-f3
			paths.append(4)
		paths.append(5)
		assert f3 >= 0
		l1 = f3**0.5
		return l1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))