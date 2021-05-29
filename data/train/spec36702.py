import numpy as np 

def function(x):

	l2 = x
	v5 = x
	paths = []
	try:
		if l2 < 4:
			x = 0+x
			l2 = l2-8
			paths.append(1)
		else:
			v5 = v5+3
			paths.append(2)
		if v5 <= 1:
			x = 8+x
			v5 = 4+9
			v5 = v5*x
			paths.append(3)
		else:
			l2 = v5/v5
			x = x/7
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