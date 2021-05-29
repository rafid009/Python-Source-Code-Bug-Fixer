import numpy as np 

def function(x):

	i5 = x
	l1 = 0
	paths = []
	try:
		if l1 >= 6:
			l1 = l1+7
			l1 = l1*7
			paths.append(1)
		else:
			x = 9/5
			paths.append(2)
		if i5 <= 3:
			i5 = i5-8
			paths.append(3)
		else:
			x = x/x
			i5 = l1*4
			l1 = 0+7
			paths.append(4)
		paths.append(5)
		assert i5 >= 0
		i5 = i5**0.5
		return i5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))