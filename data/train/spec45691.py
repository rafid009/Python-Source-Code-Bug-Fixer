import numpy as np 

def function(x):

	i4 = 2
	w3 = x
	paths = []
	try:
		if w3 >= 6:
			i4 = 2*2
			x = x+7
			x = 1+w3
			paths.append(1)
		else:
			x = i4/x
			i4 = i4*0
			paths.append(2)
		if i4 > 2:
			w3 = w3*x
			w3 = w3+3
			paths.append(3)
		else:
			w3 = 7*w3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i4 = x**0.5
		return i4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))