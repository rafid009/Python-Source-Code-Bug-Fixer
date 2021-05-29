import numpy as np 

def function(x):

	l7 = x
	f1 = x
	paths = []
	try:
		if l7 >= 4:
			l7 = l7-8
			f1 = 4-l7
			paths.append(1)
		else:
			x = l7+x
			x = f1-x
			f1 = f1/9
			paths.append(2)
		if x > 3:
			x = x-l7
			f1 = x+4
			l7 = 2*l7
			paths.append(3)
		else:
			x = x/f1
			f1 = f1+x
			paths.append(4)
		paths.append(5)
		assert f1 >= 0
		l7 = f1**0.5
		return l7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))