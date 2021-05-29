import numpy as np 

def function(x):

	w6 = 8
	j4 = 4
	paths = []
	try:
		if w6 <= 9:
			j4 = 8+j4
			x = x*2
			w6 = x+1
			paths.append(1)
		else:
			j4 = x-w6
			paths.append(2)
		if w6 < 7:
			x = x*1
			x = w6/6
			x = 9*x
			paths.append(3)
		else:
			w6 = w6+9
			w6 = j4/2
			paths.append(4)
		paths.append(5)
		assert w6 >= 0
		j4 = w6**0.5
		return j4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))