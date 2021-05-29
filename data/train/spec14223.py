import numpy as np 

def function(x):

	j4 = 3
	w6 = x
	x = 7
	paths = []
	try:
		if w6 > 2:
			x = 9*4
			x = x*2
			w6 = x*w6
			paths.append(1)
		else:
			j4 = j4+4
			x = x-1
			j4 = w6/6
			paths.append(2)
		if w6 >= 8:
			j4 = j4*0
			w6 = 8*w6
			paths.append(3)
		else:
			j4 = x*j4
			w6 = 7/w6
			x = x/6
			paths.append(4)
		paths.append(5)
		assert j4 >= 0
		j4 = j4**0.5
		return j4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))