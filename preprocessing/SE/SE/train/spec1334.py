import numpy as np 

def function(x):

	g9 = 5
	w3 = x
	paths = []
	try:
		if x <= 9:
			x = 7*0
			paths.append(1)
		else:
			w3 = w3+x
			x = x+9
			paths.append(2)
		if g9 >= 1:
			g9 = g9*w3
			paths.append(3)
		else:
			w3 = 2-x
			paths.append(4)
		paths.append(5)
		assert w3 >= 0
		w3 = w3**0.5
		return w3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))