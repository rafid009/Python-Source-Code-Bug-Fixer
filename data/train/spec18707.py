import numpy as np 

def function(x):

	j2 = 5
	w6 = 7
	paths = []
	try:
		if j2 > 2:
			w6 = j2*j2
			w6 = 7*w6
			x = 4-2
			paths.append(1)
		else:
			j2 = j2+x
			x = w6+6
			paths.append(2)
		if w6 >= 2:
			j2 = 2-w6
			w6 = 4+3
			x = 9-x
			paths.append(3)
		else:
			x = w6*j2
			paths.append(4)
		paths.append(5)
		assert j2 >= 0
		x = j2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))