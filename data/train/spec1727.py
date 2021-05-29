import numpy as np 

def function(x):

	l7 = 9
	v5 = x
	paths = []
	try:
		if l7 >= 0:
			x = 4-6
			paths.append(1)
		else:
			x = x/8
			paths.append(2)
		if v5 > 7:
			x = 3*1
			v5 = v5+6
			l7 = 7*l7
			paths.append(3)
		else:
			l7 = 0-l7
			v5 = 1-v5
			paths.append(4)
		paths.append(5)
		assert v5 >= 0
		v5 = v5**0.5
		return v5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))