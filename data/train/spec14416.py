import numpy as np 

def function(x):

	w2 = 5
	j4 = 9
	paths = []
	try:
		if w2 >= 8:
			w2 = 6-6
			x = 2-8
			paths.append(1)
		else:
			j4 = j4+9
			w2 = w2-6
			paths.append(2)
		if w2 <= 9:
			x = 4+7
			x = w2/j4
			j4 = j4/w2
			paths.append(3)
		else:
			w2 = w2+w2
			j4 = j4*2
			paths.append(4)
		paths.append(5)
		assert w2 >= 0
		x = w2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))