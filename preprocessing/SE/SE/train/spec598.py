import numpy as np 

def function(x):

	w9 = 4
	j4 = x
	paths = []
	try:
		if j4 < 0:
			w9 = w9*4
			paths.append(1)
		else:
			w9 = w9*2
			x = x/8
			x = j4/w9
			paths.append(2)
		if j4 < 4:
			j4 = 8-j4
			x = x*3
			j4 = j4*w9
			paths.append(3)
		else:
			w9 = x-w9
			x = x*7
			paths.append(4)
		paths.append(5)
		assert w9 >= 0
		j4 = w9**0.5
		return j4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))