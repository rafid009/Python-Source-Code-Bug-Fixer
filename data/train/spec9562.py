import numpy as np 

def function(x):

	w5 = 5
	j4 = x
	paths = []
	try:
		if x <= 4:
			j4 = j4+w5
			w5 = w5+7
			w5 = 3-w5
			paths.append(1)
		else:
			j4 = j4/9
			paths.append(2)
		if w5 < 6:
			w5 = w5-j4
			paths.append(3)
		else:
			w5 = 8-1
			w5 = w5*2
			paths.append(4)
		paths.append(5)
		assert w5 >= 0
		w5 = w5**0.5
		return w5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))