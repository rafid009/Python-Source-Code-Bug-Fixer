import numpy as np 

def function(x):

	a2 = x
	w7 = x
	paths = []
	try:
		if w7 >= 7:
			a2 = 5*2
			paths.append(1)
		else:
			a2 = 5/7
			x = 3*6
			paths.append(2)
		if w7 < 1:
			w7 = 9*1
			a2 = 3/9
			a2 = a2+w7
			paths.append(3)
		else:
			a2 = a2-6
			paths.append(4)
		paths.append(5)
		assert a2 >= 0
		w7 = a2**0.5
		return w7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))