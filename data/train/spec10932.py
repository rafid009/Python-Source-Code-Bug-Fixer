import numpy as np 

def function(x):

	u3 = x
	w2 = x
	paths = []
	try:
		if x < 3:
			w2 = u3/w2
			paths.append(1)
		else:
			x = x/3
			paths.append(2)
		if x <= 0:
			w2 = 9/w2
			u3 = 5+u3
			paths.append(3)
		else:
			u3 = u3*6
			u3 = w2+0
			x = 9+0
			paths.append(4)
		paths.append(5)
		assert u3 >= 0
		w2 = u3**0.5
		return w2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))