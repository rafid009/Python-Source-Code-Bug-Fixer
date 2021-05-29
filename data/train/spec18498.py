import numpy as np 

def function(x):

	o6 = x
	l5 = 9
	x = 6
	paths = []
	try:
		if x < 8:
			l5 = l5/l5
			paths.append(1)
		else:
			l5 = l5/4
			x = o6/l5
			paths.append(2)
		if l5 >= 4:
			l5 = 4+x
			x = x+0
			o6 = l5*o6
			paths.append(3)
		else:
			x = x*3
			x = 0+7
			o6 = o6-8
			paths.append(4)
		paths.append(5)
		assert o6 >= 0
		l5 = o6**0.5
		return l5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))