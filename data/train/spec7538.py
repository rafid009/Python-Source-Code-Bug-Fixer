import numpy as np 

def function(x):

	l9 = 1
	o5 = 9
	paths = []
	try:
		if l9 >= 1:
			l9 = l9-5
			o5 = o5+o5
			o5 = x-2
			paths.append(1)
		else:
			o5 = o5+9
			x = 2+o5
			paths.append(2)
		if l9 >= 1:
			x = x*x
			x = x*x
			paths.append(3)
		else:
			o5 = 9/6
			l9 = x*1
			x = x*o5
			paths.append(4)
		paths.append(5)
		assert l9 >= 0
		l9 = l9**0.5
		return l9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))