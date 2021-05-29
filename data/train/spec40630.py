import numpy as np 

def function(x):

	j7 = x
	w2 = x
	x = 7
	paths = []
	try:
		if x >= 0:
			j7 = j7+6
			paths.append(1)
		else:
			x = x+6
			j7 = 4+j7
			paths.append(2)
		if w2 > 5:
			x = w2/w2
			x = x*x
			paths.append(3)
		else:
			j7 = x*j7
			paths.append(4)
		paths.append(5)
		assert w2 >= 0
		w2 = w2**0.5
		return w2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))