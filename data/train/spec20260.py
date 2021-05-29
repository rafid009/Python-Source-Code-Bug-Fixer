import numpy as np 

def function(x):

	o5 = 4
	l6 = 3
	paths = []
	try:
		if l6 > 7:
			o5 = 5*0
			paths.append(1)
		else:
			o5 = o5+7
			o5 = o5+6
			l6 = 3-6
			paths.append(2)
		if l6 >= 3:
			o5 = l6*o5
			x = 8/x
			paths.append(3)
		else:
			l6 = 4/1
			x = 9*x
			o5 = x/o5
			paths.append(4)
		paths.append(5)
		assert o5 >= 0
		l6 = o5**0.5
		return l6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))