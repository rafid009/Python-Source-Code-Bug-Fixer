import numpy as np 

def function(x):

	k6 = 2
	l5 = x
	x = 4
	paths = []
	try:
		if l5 < 3:
			x = l5/x
			x = x+2
			x = x-8
			paths.append(1)
		else:
			l5 = 1*0
			paths.append(2)
		if k6 <= 0:
			l5 = 9-x
			l5 = l5/7
			paths.append(3)
		else:
			k6 = 4/k6
			paths.append(4)
		paths.append(5)
		assert l5 >= 0
		k6 = l5**0.5
		return k6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))