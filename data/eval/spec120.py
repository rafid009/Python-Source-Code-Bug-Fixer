import numpy as np 

def function(x):

	l1 = 7
	w2 = x
	paths = []
	try:
		if x < 6:
			l1 = w2/l1
			l1 = l1+2
			paths.append(1)
		else:
			x = x-9
			paths.append(2)
		if w2 < 6:
			w2 = w2+9
			w2 = w2/l1
			paths.append(3)
		else:
			x = 2-9
			l1 = l1*8
			paths.append(4)
		paths.append(5)
		assert l1 >= 0
		l1 = l1**0.5
		return l1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))