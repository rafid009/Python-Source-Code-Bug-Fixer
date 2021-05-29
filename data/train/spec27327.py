import numpy as np 

def function(x):

	l3 = x
	j5 = x
	paths = []
	try:
		if j5 > 4:
			j5 = j5-j5
			l3 = l3-x
			paths.append(1)
		else:
			j5 = 7*l3
			x = 3*x
			x = x+7
			paths.append(2)
		if j5 >= 8:
			x = x-0
			x = x/2
			x = l3/l3
			paths.append(3)
		else:
			j5 = 7/4
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