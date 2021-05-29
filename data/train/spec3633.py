import numpy as np 

def function(x):

	l3 = x
	j7 = 1
	paths = []
	try:
		if j7 < 8:
			j7 = 8/6
			x = x-9
			l3 = x/l3
			paths.append(1)
		else:
			j7 = j7/j7
			x = l3-l3
			j7 = l3-6
			paths.append(2)
		if l3 < 3:
			l3 = 7/l3
			x = x-7
			x = x+9
			paths.append(3)
		else:
			x = 2*7
			j7 = 4-j7
			j7 = j7-j7
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