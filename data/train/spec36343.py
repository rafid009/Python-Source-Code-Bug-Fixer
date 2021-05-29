import numpy as np 

def function(x):

	l6 = x
	v6 = 0
	paths = []
	try:
		if x > 9:
			v6 = 1/2
			x = x/7
			paths.append(1)
		else:
			v6 = 1*v6
			paths.append(2)
		if l6 > 5:
			v6 = v6+3
			x = x-2
			paths.append(3)
		else:
			v6 = 7/l6
			paths.append(4)
		paths.append(5)
		assert v6 >= 0
		l6 = v6**0.5
		return l6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))