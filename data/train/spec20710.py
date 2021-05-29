import numpy as np 

def function(x):

	l2 = x
	o0 = 1
	paths = []
	try:
		if x <= 0:
			l2 = l2+9
			o0 = o0/o0
			x = x*4
			paths.append(1)
		else:
			l2 = 6-2
			paths.append(2)
		if l2 >= 8:
			o0 = 1-o0
			x = 7+7
			o0 = o0-1
			paths.append(3)
		else:
			o0 = o0-x
			x = 1-x
			l2 = 6*0
			paths.append(4)
		paths.append(5)
		assert o0 >= 0
		l2 = o0**0.5
		return l2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))