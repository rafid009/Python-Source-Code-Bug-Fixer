import numpy as np 

def function(x):

	w7 = x
	a1 = x
	x = 6
	paths = []
	try:
		if w7 <= 7:
			x = 5/7
			w7 = 0*4
			a1 = a1/2
			paths.append(1)
		else:
			a1 = 9+a1
			paths.append(2)
		if x < 8:
			x = a1+0
			w7 = w7*6
			w7 = w7-7
			paths.append(3)
		else:
			x = x+w7
			w7 = w7/x
			w7 = w7/9
			paths.append(4)
		paths.append(5)
		assert a1 >= 0
		a1 = a1**0.5
		return a1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))