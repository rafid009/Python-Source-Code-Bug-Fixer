import numpy as np 

def function(x):

	w7 = x
	n3 = 8
	paths = []
	try:
		if n3 > 2:
			w7 = w7*0
			paths.append(1)
		else:
			w7 = x/w7
			x = 1*x
			x = 5*x
			paths.append(2)
		if n3 <= 5:
			w7 = w7+8
			n3 = n3+0
			w7 = 5+7
			paths.append(3)
		else:
			n3 = n3*x
			w7 = 4+w7
			paths.append(4)
		paths.append(5)
		assert n3 >= 0
		x = n3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))