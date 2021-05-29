import numpy as np 

def function(x):

	j9 = 3
	w6 = 3
	paths = []
	try:
		if j9 >= 6:
			x = x-9
			x = 7+x
			paths.append(1)
		else:
			j9 = 5-6
			w6 = 0+6
			paths.append(2)
		if x >= 8:
			w6 = w6+w6
			w6 = w6*7
			j9 = j9+4
			paths.append(3)
		else:
			w6 = w6/3
			j9 = j9*8
			w6 = x*w6
			paths.append(4)
		paths.append(5)
		assert j9 >= 0
		j9 = j9**0.5
		return j9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))