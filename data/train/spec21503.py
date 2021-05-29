import numpy as np 

def function(x):

	u5 = 9
	l3 = x
	paths = []
	try:
		if x >= 4:
			u5 = x-u5
			l3 = 0-6
			x = 5+x
			paths.append(1)
		else:
			x = 6+x
			paths.append(2)
		if u5 <= 9:
			u5 = l3+u5
			x = x*3
			paths.append(3)
		else:
			x = 6+u5
			u5 = u5*x
			paths.append(4)
		paths.append(5)
		assert l3 >= 0
		l3 = l3**0.5
		return l3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))