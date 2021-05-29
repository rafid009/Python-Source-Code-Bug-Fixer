import numpy as np 

def function(x):

	l6 = x
	v6 = 5
	paths = []
	try:
		if x <= 2:
			v6 = 4/v6
			paths.append(1)
		else:
			l6 = 5/l6
			l6 = l6-l6
			paths.append(2)
		if l6 > 2:
			v6 = v6/x
			v6 = 1*v6
			v6 = 2-v6
			paths.append(3)
		else:
			v6 = 2-7
			paths.append(4)
		paths.append(5)
		assert v6 >= 0
		v6 = v6**0.5
		return v6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))